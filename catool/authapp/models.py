from django.db import models
from catapp.models import Client,Account
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self,email,first_name,password=None,active=True,admin=False,staff=False):
        if not email or not password:
            raise ValueError("Please specify correct email and password.")
        user=self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name=first_name
        user.staff = staff
        user.active = active
        user.admin = admin
        user.save()
        return user

    def create_staff(self,email,first_name,password=None):
        user=self.create_user(email,first_name,password=password,staff=True)
        return user

    def create_superuser(self,email,first_name,password=None):
        user=self.create_user(email,first_name,password=password,staff=True,admin=True)
        return user

class User(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=255,unique=True)
    account=models.ForeignKey(Account,on_delete=models.PROTECT,null=True)
    createdon=models.DateTimeField(auto_now_add=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(null=True, blank=True)
    avatar=models.FileField(upload_to='files/',null=True,blank=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        return '%s %s'%(self.first_name,self.last_name)

    def get_short_name(self):
        return self.first_name

    def email_user(self,subject,message,from_email=None,**kwargs):
        # send_mail(subject,message,from_email,[self.email],**kwargs)
        pass

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def has_perm(self,perm, obj=None):
        return True

    def has_module_perms(self,app_label):
        return True






