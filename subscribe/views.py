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
from django.conf import settings
import logging
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        contactForm = SubscribeForm(request.POST)
        if contactForm.is_valid():
            instance = contactForm.save(commit=False)
            if subscribeUs.objects.filter(email=instance.email).exists():
                messages.warning(request,'This email address is already in use.')
            else:
                contactForm.save()
                messages.success(request, 'Thanks for Subscribing to our Newsletter. Please check your email for news udpates.')
                userEmailAdd = request.POST['email']
                subject = 'Welcome to MoIC Newsletter Subcription'
                message = 'Sir/Madam : You are receiving this email because you subscribed to the MoIC NewsLetter.'
                sender = settings.EMAIL_HOST_USER
                to = [userEmailAdd]
            # msg = EmailMultiAlternatives(subject,text_content,sender,to=[userEmailAdd])
            # msg.attach_alternative(msg, "text/html")
            # msg.send()
                send_mail(subject, message,sender,to)
                return redirect('/subscribe')
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
