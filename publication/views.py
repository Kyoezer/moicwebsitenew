from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def policies(request):
    policies = policy.objects.all()
    context = {'policies': policies}
    return render(request, 'policies.html', context)


def acts(request):
    acts = arts.objects.all()
    context = {'acts': acts}
    return render(request, 'acts.html', context)


def rules(request):
    rules = rule.objects.all()
    context = {'rules': rules}
    return render(request, 'rules.html', context)


def regulations(request):
    regulations = regulation.objects.all()
    context = {'regulations': regulations}
    return render(request, 'rules.html', context)


def guidelines(request):
    guidelines = guideline.objects.all()
    context = {'guidelines': guidelines}
    return render(request, 'guidelines.html', context)


def reports(request):
    reports = report.objects.all()
    context = {'reports': reports}
    return render(request, 'reports.html', context)


def statistics(request):
    statistics = statistic.objects.all()
    context = {'statistics': statistics}
    return render(request, 'statistics.html', context)
