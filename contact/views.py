
from contact.forms import ContactForm

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            subject = "Website Inquiry"
            body = {
            'first_name': contactForm.cleaned_data['first_name'],
            'last_name': contactForm.cleaned_data['last_name'],
            'email': contactForm.cleaned_data['email_address'],
            'message':contactForm.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            messages.success(request, 'You have successfully contacted to MoIC')

            try:
                send_mail(subject, message, 'email', ['admin@moic.gov.bt'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/contact")
    return render(request, "contact.html", {'form': form})
#
	# form = ContactForm()
