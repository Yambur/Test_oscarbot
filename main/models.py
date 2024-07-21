from django.db import models
import uuid

from config.settings import AUTH_USER_MODEL


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='tasks')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
