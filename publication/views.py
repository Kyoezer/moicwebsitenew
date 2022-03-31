from django.shortcuts import render

# Create your views here.
def policies(request):
    return render(request, 'policies.html',)


def acts(request):
    return render(request, 'acts.html',)


def rules(request):
    return render(request, 'rules.html',)


def guidelines(request):
    return render(request, 'guidelines.html',)


def reports(request):
    return render(request, 'reports.html',)


def statistics(request):
    return render(request, 'statistics.html',)