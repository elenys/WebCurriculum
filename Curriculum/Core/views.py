from django.shortcuts import render
from Portfolio.models import Project
# Create your views here.


def index(request):
    projects = Project.objects.all()
    return render(request, 'Core/index.html', {'all_projects': projects})