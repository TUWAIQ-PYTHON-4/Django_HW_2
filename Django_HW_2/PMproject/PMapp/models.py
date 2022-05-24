from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    cr_time = models.DateTimeField('creating_time')
    com_time = models.DateTimeField('completion_time')

class Task(models.Model):
    title = models.CharField(max_length=200)
    de_ = models.DateTimeField('description')
    time_es = models.IntegerField('time estimate', default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


def __str__(self):
        return self.name

