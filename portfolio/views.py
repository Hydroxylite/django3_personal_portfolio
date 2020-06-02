from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    #grabs all objects out of the data, turns them into objects
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {'projects':projects})
