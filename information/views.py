from django.shortcuts import render

# Create your views here.
def moicofficials(request):
    
    return render(request, 'moicofficials.html', )


def download(request):
    
    return render(request, 'download.html', )


def hrdecisions(request):
    
    return render(request, 'hrdecisions.html', )


def rsrstaservices(request):
    
    return render(request, 'rstaservices.html', )
