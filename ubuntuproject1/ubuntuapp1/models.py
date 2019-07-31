from django.db import models
import uuid
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
import datetime
# Create your models here.

class State(models.Model):
    name=models.CharField(max_length=100,unique=True,verbose_name='Name of State')
    active=models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

class School(models.Model):
    SCHOOL_TYPE=(
        (1,'State Board'),
        (2,"CBSE"),
        (3,"ICSC"),
        (4,"Other")
    )
    sid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=150,verbose_name='Name of School',unique=True)
    schooltype=models.SmallIntegerField(choices=SCHOOL_TYPE,default=1)
    capacity=models.PositiveIntegerField(validators=[MinValueValidator(100)])
    staffcapacity=models.IntegerField(validators=[MinValueValidator(1)])
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    address=models.CharField(max_length=255,verbose_name='Address')
    longitude=models.CharField(max_length=25,null=True,blank=True)
    latitude = models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

def date_check(value):
    pass

class Teacher(models.Model):
    TEACHER_TYPE=(
        (0,'Active'),
        (1,'Inactive')
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=125,verbose_name='Name of Teacher')
    adhar_number=models.CharField(max_length=12,verbose_name='Adhar Number')
    mobile=models.IntegerField(verbose_name='Mobile Number')
    tenthperc=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)
    twelthperc=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)
    ugperc=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)
    pgperc=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)
    joiningdate=models.DateTimeField()
    createddate=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    designation=models.CharField(max_length=25,verbose_name='Designation')
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    status=models.SmallIntegerField(default=0,choices=TEACHER_TYPE)
    experience=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        unique_together=('adhar_number','mobile')

class Subject(models.Model):
    name=models.CharField(max_length=25, verbose_name='Name of Subject')

    def __str__(self):
        return self.name

class TeachSub(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time=models.TimeField(null=True)


class PreviousExp(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    lastschool=models.CharField(max_length=150,verbose_name='Previous School name')
    fromdate=models.DateField(null=True)
    todate=models.DateField(null=True)
