from django.shortcuts import render
from Presentation.models import Profile


def presentation(request):
    profile = Profile.objects.all()
    return render(request, 'Presentation/presentation.html', {'profile': profile})
