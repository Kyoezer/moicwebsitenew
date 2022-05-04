from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
from django.core.files import File
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class hrdecisions(models.Model):
    content = RichTextField(blank=True)
    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')