from django.db import models

class Project(models.Model):
    name=models.CharField(max_length=100 , help_text ='this is name')
    creation_time=models.DateTimeField(auto_now_add=True , help_text='this is creation time')
    completion_time=models.DateTimeField(null= True, help_text='this is completiontime')

class Task(models.Model):
    title=models.CharField(max_length = 100, help_text = 'this is title')
    description=models.TextField(help_text='this is description')
    time_estimate=models.IntegerField(help_text ='time_estimate')
    completed=models.BooleanField(default = False)