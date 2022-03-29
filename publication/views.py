from django.shortcuts import render

# Create your views here.
def publication(request):
    return render(request, 'publication.html',)