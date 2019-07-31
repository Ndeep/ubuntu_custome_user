from django.db import models

# Create your models here.

class Client(models.Model):
    client_id=models.AutoField(primary_key=True,db_column='c_id')
    client_name=models.CharField(max_length=255,unique=True,db_column='c_name')
    is_active=models.SmallIntegerField(max_length=1,default=1)

    def __str__(self):
        return self.client_name


class Account(models.Model):
    account_id=models.AutoField(primary_key=True,db_column='acc_id')
    account_name=models.CharField(max_length=255,unique=True,db_column='acc_name')
    client=models.ForeignKey(Client,on_delete=models.PROTECT)
    is_active=models.SmallIntegerField(max_length=1,default=1)

    def __str__(self):
        return self.account_name



