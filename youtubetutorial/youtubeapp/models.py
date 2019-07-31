from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=255)
    created_by=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'time': self.created_by,
            'user_id': self.user.id,
            'status': self.status
        }
