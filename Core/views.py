from django.shortcuts import render
from Portfolio.models import Project
from Contact.form import ContactForm
from django.core.mail import send_mail
from Presentation.models import Profile


def index(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.name = form.cleaned_data['name']
            form.message = form.cleaned_data['message']
            form.sender = form.cleaned_data['sender']
            form.copy = form.cleaned_data['copy']
            # recipients = ['elhensar@gmail.com']
            # if form.copy:
            #     recipients.append(form.sender)
            # send_mail(form.name, form.message, form.sender, recipients)
            form.valid = True
    else:
        form = ContactForm()
    return render(request, 'Core/index.html', {'profiles': profiles, 'projects': projects, 'form': form})