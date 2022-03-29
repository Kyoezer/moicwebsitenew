from datetime import datetime
from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# annual report
class select_annual_report(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = RichTextField()
    short_link = models.CharField(max_length=400, blank=True)
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    pub_date = models.DateTimeField('date published')

class social_link(models.Model):
    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

# ANNUAL PERFORMANCE AGREEMENT
class annual_performance_agreement(models.Model):
    title =  models.CharField(max_length=400, blank=True)
    address_link =  models.CharField(max_length=200, blank=True)