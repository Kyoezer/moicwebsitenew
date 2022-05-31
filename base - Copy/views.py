from django.shortcuts import render
from base.models import ImageGallery


# Create your views here.
def gallery(request):
    images = ImageGallery.objects.all()
    return render(request, 'base.html', {'images', images})
