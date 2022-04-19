from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class media_gallery(models.Model):
    images = models.ImageField(blank=True, upload_to='pics')
    image_description = RichTextField(blank=True)
