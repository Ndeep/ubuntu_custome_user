from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
# Create your models here.

#python manage.py dumpdata authenticatiosapp --format json --indent 4 > authenticatiosapp/fixtures/user.json


class UserManager(BaseUserManager):
    def create_user(self,email,first_name,password=None,active=True,staff=False,admin=False):
        if not email and not password:
            raise ValueError("")
        user=self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name = first_name
        user.staff=staff
        user.active=active
        user.admin=admin
        user.save()
        return user

    def create_staff(self,email,first_name,password=None):
        user=self.create_user(
            email,
            first_name,
            password=password,
            staff=True
        )
        return user

    def create_superuser(self,email,first_name,password=None):
        user=self.create_user(
            email,
            first_name,
            staff=True,
            admin=True
        )
        return user

class User(AbstractBaseUser):
    email=models.EmailField(max_length=255,unique=True)
    mobile=models.IntegerField(max_length=10,blank=True,null=True)
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    confirmed=models.BooleanField(default=False)
    confirmed_date=models.DateTimeField(null=True,blank=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

