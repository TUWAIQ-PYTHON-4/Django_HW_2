from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, help_text='The name of the project')
    creation_time = models.DateField(auto_now_add=True, help_text='The project creation time')
    completion_time= models.DateTimeField(null=True, help_text='The project completion time')

class Task(models.Model):
    title = models.CharField(max_length=100, help_text='The title of a task')
    description = models.TextField(help_text='The task description')
    time_estimate = models.IntegerField(help_text='Task time estimate')
    completed = models.BooleanField(default=False)