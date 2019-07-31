import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class AutoTimestamp(models.Model):
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(AutoTimestamp):
    """
    Post model for blog section of website
    """
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    picture = models.TextField(null=True,blank=True)
    description = models.TextField(default='No post description',null=True,blank=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True)

    def __str__(self):
        return self.title