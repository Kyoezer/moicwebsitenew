from datetime import datetime
from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.files import File

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
    title = models.CharField(max_length=400, blank=True)
    YEAR = (
        ('2014-2015', '2014-2015'),
        ('2016-2017', '2016-2017'),
        ('2017-2018', '2017-2018'),
        ('2018-2019', '2018-2019'),
        ('2019-2020', '2019-2020'),
        ('2020-2021', '2020-2021'),
        ('2021-2022', '2021-2022'),
        ('2022-2023', '2022-2023'),
        ('2023-2024', '2023-2024'),
    )
    year = models.CharField(choices=YEAR, max_length=100, null='True', blank='True')
    attachment = models.FileField(blank=True, null=True, upload_to='files')
