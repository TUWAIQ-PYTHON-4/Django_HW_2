from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150, help_text="project name")
    date = models.DateField(auto_now_add=True, help_text="Date the Prject .")
    completion_time = models.DateField(True, help_text="Completion time.")
    def __str__(self):
        return self.name

class Task(models.Model):
    Project =models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, help_text="title")
    description = models.TextField(help_text="Description")
    time_estimate = models.IntegerField(help_text="Time")
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title