from django.shortcuts import render
from .models import annual_performance_agreement


# Create your views here.
def annual1(request):
    annual = annual_performance_agreement.objects.all()
    context = {'annual': annual}
    return render(request, 'annual1.html', context)

def annual2(request):
    
    return render(request, 'annual2.html', )


def annual3(request):
    
    return render(request, 'annual3.html', )