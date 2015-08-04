from django.shortcuts import render
# Create your views here.
from Presentation.models import Profile


def index(request):
    profiles = Profile.objects.all()
    return render(request, 'Core/index.html', {'profiles': profiles})