from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class Client(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

    @property
    def accounts(self):
        return self.account_set.all()


class Account(models.Model):
    name=models.CharField(max_length=25)
    client=models.ForeignKey(Client,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    @property
    def users(self):
        return self.user_set.all()


class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,active=True,staff=False,admin=False):
        if not username and not email and not password:
            raise ValueError("Provide email/Username/Password")
        user=self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.staff=staff
        user.active=active
        user.admin=admin
        user.save(using=self._db)
        return user

    def create_staff(self,username,email,password=None,active=True,staff=True,admin=False):
        user=self.create_user(username,email,password,active,staff,admin)
        return user

    def create_superuser(self,username,email,password=None,active=True,staff=True,admin=True):
        user=self.create_user(username,email,password,active,staff,admin)
        return user


class User(AbstractBaseUser):
    username=models.CharField(max_length=25,unique=True)
    email=models.EmailField(max_length=125,unique=True)
    account=models.ForeignKey(Account,on_delete=models.PROTECT)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=True)
    admin=models.BooleanField(default=True)

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
