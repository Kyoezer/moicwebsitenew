from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def moicofficials(request):
    
    return render(request, 'moicofficials.html', )


def download(request):
    
    return render(request, 'download.html', )


def hrdecision(request):
    # paginator
    p = Paginator(hrdecisions.objects.all().order_by('-id'), 5)
    page = request.GET.get('page')
    hr = p.get_page(page)

    return render(request, 'hrdecisions.html', {'hr': hr})


def rsrstaservices(request):
    
    return render(request, 'rstaservices.html',)


def terms(request):

    return render(request, 'terms.html')


def privacy(request):

    return render(request, 'privacy.html')


def disclaimer(request):

    return render(request, 'disclaimer.html')
