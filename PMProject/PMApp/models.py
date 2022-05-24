from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=120, help_text="Project name")
    date = models.DateField(auto_now_add=True, help_text="Date the Prject .")
    completion_time = models.DateField(True, help_text="Completion time.")
    def __str__(self):
        return self.name

class Task(models.Model):
    Project =models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=120, help_text="title")
    description = models.TextField(help_text="this is Description")
    time_estimate = models.IntegerField(help_text="Time")
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title