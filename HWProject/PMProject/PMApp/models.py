from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, help_text="help")
    creation_time = models.DateTimeField(auto_now_add=True,help_text="help")
    completion_time = models.DateTimeField(null=True,help_text="help")

class Task(models.Model):
    title  = models.CharField(max_length=100, help_text="help")
    description  = models.TextField( help_text="help")
    time_estimate  = models.IntegerField( help_text="help")
    completed = models.BooleanField(default=False)



