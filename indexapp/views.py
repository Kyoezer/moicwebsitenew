from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from indexapp.models import post
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    popuplarPs = post.objects.all()
    return render(request, 'home.html', {'post': popuplarPs, })


    

