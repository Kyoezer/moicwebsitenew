from django.shortcuts import render
from .models import *

# Create your views here.


def whoiswho(request):
    ministeroffice = office_of_minister.objects.all()
    secretaryoffice = office_of_secretary.objects.all()
    ppd = policy_planning_division.objects.all()
    hrd = human_resource_division.objects.all()
    ictd = ict_division.objects.all()
    ia = internal_audit.objects.all()
    adm = administration.objects.all()
    fd = finance_division.objects.all()
    ps = procurement_section.objects.all()
    context = {'ministeroffice': ministeroffice,
                'secretaryoffice': secretaryoffice,
                'ppd': ppd,
                'hrd': hrd,
                'ictd': ictd,
                'ia': ia,
                'adm': adm,
                'fd': fd,
                'ps': ps,
                }
    return render(request, 'whoiswho.html', context,)
