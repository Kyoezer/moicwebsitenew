from django.db import models


class ImageGallery(models.Model):
    image = models.ImageField(blank=True, upload_to='pics')
    caption = models.CharField(null=True, max_length=200)


# Create your models here.
