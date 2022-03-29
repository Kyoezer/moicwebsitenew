from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class background(models.Model):
    histroy_title = models.CharField(max_length=200)
    histroy_content = RichTextField()
    histroy_img = models.ImageField(blank=True,upload_to='pics')

    secound01_histroy_content = RichTextField()
    secound_histroy_img = models.ImageField(blank=True,upload_to='pics')
    secound02_histroy_content = RichTextField()

# MINISTRY HISTORY
class Ministry_Histroy(models.Model):
    title = models.CharField(max_length=100)
    year_establish = models.CharField(max_length=100)
    year_establish_title = models.CharField(max_length=100)
    # part time models
    establish_description_title = models.CharField(max_length=200)
    establish_description = RichTextField(blank=True)

# MINISTRY TIMELINE
class Ministry_Timeline(models.Model):
    title = models.CharField(max_length=100)
    year_in = models.CharField(max_length=100)
    year_establish_name = models.CharField(max_length=100)
    # part time models 
    establish_description_img = models.ImageField(blank=True,upload_to='pics')
    establish_description = RichTextField(blank=True)

# TIMELINE OF SECRETARIES
class Secretaries_Timeline(models.Model):
    title = models.CharField(max_length=100)
    year_in = models.CharField(max_length=100)
    year_establish_name = models.CharField(max_length=100)
    # part time models 
    establish_description_img = models.ImageField(blank=True,upload_to='pics')
    establish_description = RichTextField(blank=True)

# MEMBERSHIP
class membership(models.Model):
    si_no = models.IntegerField()
    Name_of_International_and_Regional_org = models.CharField(max_length=200)
    Membership_Joining_Date = models.IntegerField()

# ABOUT US
class about_u(models.Model):
    title = models.CharField(max_length=100)
    url_address = models.CharField(max_length=300)
    	
 