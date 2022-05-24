from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, help_text="Name..")
    creation_time = models.DateField(verbose_name="create time")
    completion_time = models.DateField(verbose_name2="completion time")


class Task(models.Model):
    title = models.CharField(max_length=100, TextField="The title....")
    description = models.TextField(TextField="description ")
    date = models.DateField(verbose_name3="Date the Movie was released.")
    time_estimate = models.IntegerField(help_text="time_estimate")
    completed = models.BooleanField(False)
