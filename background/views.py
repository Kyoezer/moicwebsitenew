from django.shortcuts import render

# Create your views here.
def background(request):
    
    return render(request, 'background.html', )