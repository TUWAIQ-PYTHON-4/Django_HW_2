from django.shortcuts import render
# Create your views here.

def list():
    x = Task.object.all()
    context = {key.value}
