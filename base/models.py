from django.db import models

class ImageGallery(models.Model):
    gallery_img = models.ImageField(blank=True,upload_to='pics')
    gallery_description = models.CharField(null = True, max_length=200)


# Create your models here.
