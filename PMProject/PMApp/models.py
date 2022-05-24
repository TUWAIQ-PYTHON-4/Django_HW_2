from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, help_text='project name')
    creation_time = models.DateTimeField(auto_now_add=True, help_text='creation time')
    completion_time = models.DateTimeField(help_text='completion time', null=True)


class Task(models.Model):
    title = models.CharField(max_length=100, help_text='Task name')
    description = models.TextField(help_text='Task name')
    time_estimate = models.IntegerField(help_text='creation time')
    completed = models.BooleanField(default=False)
