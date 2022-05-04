from django.shortcuts import render
from .models import *


# Create your views here.
def moicofficials(request):
    
    return render(request, 'moicofficials.html', )


def download(request):
    
    return render(request, 'download.html', )


def hrdecision(request):
    hrds = hrdecisions.objects.all()
    return render(request, 'hrdecisions.html', {'hrds': hrds})


def rsrstaservices(request):
    
    return render(request, 'rstaservices.html', )
