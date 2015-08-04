from django.shortcuts import render
# Create your views here.
from Presentation.models import Profile
from Portfolio.models import Project


def index(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'Core/index.html', {'profiles': profiles, 'projects': projects})