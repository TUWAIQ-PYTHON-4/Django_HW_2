from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length = 100, help_text = 'Project Name')
    creation_time = models.DateTimeField(auto_now_add = True, help_text = 'Creation Time')
    completion_time = models.DateTimeField(None, help_text = 'Completion time')

class Task(models.Model):
    Project = models.ForeignKey(Project, on_delete= models.CASCADE)
    title = models.CharField(max_length = 100, help_text = 'Task Title')
    description = models.TextField(help_text = 'Task description')
    time_estimate = models.IntegerField(help_text = 'Estimated time')
    completed = models.BooleanField(default=False)