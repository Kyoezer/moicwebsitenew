from django.shortcuts import render
from base.models import ImageGallery


# Create your views here.
def base(request):
    pictures = ImageGallery.objects.all()
    return render(request, 'base.html', {'pictures', pictures})
