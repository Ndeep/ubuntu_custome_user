from django.db import models

# Create your models here.
class Tax(models.Model):
    name=models.CharField(max_length=25)
    delete=models.BooleanField(default=True)

class TaxDetail(models.Model):
    tax=models.ForeignKey(Tax,on_delete=models.CASCADE)
    effectivefromdate=models.DateTimeField()
    effectivetodate=models.DateTimeField()

