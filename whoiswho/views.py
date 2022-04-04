from django.shortcuts import render
from .models import *

# Create your views here.


def whoiswho(request):
    ministeroffice = office_of_minister.objects.all()
    secretaryoffice = office_of_secretary.objects.all()
    context = { 'ministeroffice': ministeroffice,
                'secretaryoffice': secretaryoffice}
    return render(request, 'whoiswho.html', context,)
