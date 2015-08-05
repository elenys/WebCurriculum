from Contact.form import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render


def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.name = form.cleaned_data['subject']
            form.message = form.cleaned_data['message']
            form.sender = form.cleaned_data['sender']
            form.copy = form.cleaned_data['cc']
            recipients = ['elhensar@gmail.com']
            if form.cc:
                recipients.append(form.sender)
            send_mail(form.subject, form.message, form.sender, recipients)
            form.valid = True
    else:
        form = ContactForm()
    return render(request, 'Contact/Contact.html', {'form': form})