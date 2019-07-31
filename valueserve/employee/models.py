from django.db import models
from django.utils.translation import ugettext_lazy as _
from authenticationapp.models import User
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.
class Department(models.Model):
    dept_no = models.CharField(_('code'), primary_key=True, max_length=4)
    dept_name = models.CharField(_('name'), unique=True, max_length=40)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        db_table = 'departments'
        ordering = ['dept_no']

    def __str__(self):
        return self.dept_name

def validate_dob(value):
    if date.today().year-value.year<18:
        raise ValidationError('Date of birth should be greater then 18.')

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,db_column='user_id')
    emp_no = models.IntegerField(_('employee number'), primary_key=True)
    birth_date = models.DateField(_('birthday'),validators=[validate_dob])
    gender = models.CharField(_('gender'), max_length=1)
    department=models.ForeignKey(Department,on_delete=models.PROTECT,db_column='depart_id')
    hire_date = models.DateField(_('hire date'),auto_now_add=True)

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employees'

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    salary = models.IntegerField(_('salary'))
    from_date = models.DateField(_('from'))
    to_date = models.DateField(_('to'))


    class Meta:
        db_table = 'salaries'
        ordering = ['-from_date']
        verbose_name = _('salary')
        verbose_name_plural = _('salaries')

    def __str__(self):
        return "{} - {}".format(self.employee, self.salary)
