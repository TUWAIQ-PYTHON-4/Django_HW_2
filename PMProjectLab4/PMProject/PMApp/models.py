from django.db import models



class Project(models.Model):
    name = models.CharField(max_length = 110 , help_text = "The name of the Project.")
    creation_time = models.DateTimeField(auto_now_add=True , help_text="The is creatig time")
    completion_time = models.DateTimeField( null= False , help_text= "The is completion time")

class Task(models.Model):
    title = models.CharField(max_length= 110 , help_text= "The title of the Task.")
    description= models.TextField( help_text= "  ")
    time_estimate = models.IntegerField(help_text= "  ")
    completed = models.BooleanField(default = False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

