import null as null
from django.db import models
from collections import MutableMapping, MutableSequence

class Project(models.Model):
    name = models.CharField(max_length=100, help_text="project name")
    date = models.DateField(auto_now_add=True, help_text="Date the Prject .")
    completion_time = models.DateField(null, help_text="Completion time.")


class Task(models.Model):
    title = models.CharField(max_length=100, help_text="Task name")
    description = models.TextField(help_text="Task Help.")
    time_estimate = models.IntegerField(help_text="Task time.")
    completed = models.BooleanField(default=False)
