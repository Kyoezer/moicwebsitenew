from email import message
from subscribe.forms import SubscribeForm, MailMessageForm
from django.contrib import messages
from django_pandas.io import read_frame
from django.shortcuts import render, redirect
from .forms import SubscribeForm, MailMessageForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import subscribeUs
import logging


# Create your views here.

def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        contactForm = SubscribeForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscribeForm()
        context = {
            'form': form,
        }
    return render(request, "subscribe.html", {'form': form})


def mail_letter(request):
    # send_mail(
    # 'tNew post check',
    # 'Here is the message.',
    # 'yesdorji@gmail.com',
    # ['ydorji@moic.gov.bt'],
    # fail_silently=False,
    # )
    # send_mail('test email','texting message','ydorji@moic.gov.bt',['yesdorji@gmail.com'],fail_silently=False)
    # form = MailMessageForm()
    emails = subscribeUs.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    print(df)
    mail_list = df['email'].values.tolist()
    # logging.debug(mail_list)

    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('mail_letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'mail_letter.html', context)