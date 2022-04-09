from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from indexapp.models import post, event, vacancie
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    popuplarPs = post.objects.all()
    events = event.objects.all().order_by('-id')
    vacancies = vacancie.objects.all().order_by('-id')
    return render(request, 'home.html', {'post': popuplarPs, 'events': events, 'vacancies': vacancies})

def vacancy_detail (request, id):
    obj =get_object_or_404(vacancie, pk=id)
    return render(request, 'vacancy_detail.html', {'obj': obj })

def detail (request, id):
    obj =get_object_or_404(event, pk=id)
    return render(request, 'detail.html', {'obj': obj })


    

