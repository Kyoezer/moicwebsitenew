from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def moicofficials(request):
    
    return render(request, 'moicofficials.html', )


def download(request):
    
    return render(request, 'download.html', )


def hrdecision(request):
    hrds = hrdecisions.objects.all()

    # paginator
    p = Paginator(hrdecisions.objects.all(), 3)
    page = request.GET.get('page')
    hr = p.get_page(page)

    return render(request, 'hrdecisions.html', {'hrds': hrds, 'hrdecisions': hr})


def rsrstaservices(request):
    
    return render(request, 'rstaservices.html',)
