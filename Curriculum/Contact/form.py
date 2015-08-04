from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label="Your Email")
    copy = forms.BooleanField(help_text="If you want a copy of the mail", required=False)