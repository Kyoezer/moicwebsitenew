from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
from django.core.files import File
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class policy(models.Model):
    top_title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    link_title = models.CharField(max_length=100, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')


# ACTS
class arts(models.Model):
    top_title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    link_title = models.CharField(max_length=100, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')


# RULES & REGULATIONS
class rule(models.Model):
    top_title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    link_title = models.CharField(max_length=100, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')


class regulation(models.Model):
    top_title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    link_title = models.CharField(max_length=100, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')


# GUIDELINES
class guideline(models.Model):
    top_title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    link_title = models.CharField(max_length=100, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')


# REPORTS
class report(models.Model):
    top_title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    copy_link = models.CharField(max_length=400, blank=True)
    facebook = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    link_title = models.CharField(max_length=100, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')


# STATISTICS
class statistic(models.Model):
    # top_title = models.CharField(max_length=200, blank=True)
    # content = RichTextField(blank=True)
    # INFO COMM STATISTICS
    # info_icon = models.ImageField(blank=True, upload_to='pics')
    # info_count = models.IntegerField(blank=True, null=True)
    # info_title = models.CharField(max_length=200, blank=True)
    # info_info = models.CharField(max_length=200, blank=True)

    # slider
    # slider_img = models.ImageField(blank=True, upload_to='pics')
    # slider_title = models.CharField(max_length=200, blank=True)
    # slider_name = models.CharField(max_length=200, blank=True)
    # report_report = models.CharField(max_length=200, blank=True)


    # ANNUAL INFO-COMM & TRANSPORT STATISTICAL BULLETIN

    SI_No = models.IntegerField(blank=True)
    title = models.CharField(max_length=400, blank=True)
    attachment = models.FileField(blank=True, null=True, upload_to='files')
    # copy_link = models.CharField(max_length=400, blank=True)
    # facebook = models.CharField(max_length=400, blank=True)
    # whatsapp = models.CharField(max_length=400, blank=True)
    # email = models.CharField(max_length=400, blank=True)
    # telegram = models.CharField(max_length=400, blank=True)

    # title of address link
    # link_title = models.CharField(max_length=100, blank=True)
    # link_name = models.CharField(max_length=100, blank=True)

