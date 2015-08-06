from django.shortcuts import render
from Presentation.models import Profile


def presentation(request):
    profiles = Profile.objects.all()
    return {'profiles': profiles}
