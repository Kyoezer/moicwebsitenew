from django.shortcuts import render
from base.models import media_gallery
# Create your views here.


def base(request):
    pictures = media_gallery.objects.all()
    context = {'pictures': pictures}
    return render(request, 'base.html', context)
