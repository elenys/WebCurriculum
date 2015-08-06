from django.shortcuts import render

from Contact.views import contact
from Presentation.views import presentation
from Portfolio.views import portfolio


def index(request):
    profiles = presentation
    projects = portfolio
    form = contact(request)
    return render(request, 'Core/index.html', {'profiles': profiles, 'projects': projects, 'form': form})