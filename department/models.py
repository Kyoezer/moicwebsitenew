from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# DoAT
# DEPARTMENT OF AIR TRANSPORT

# Bio
class department_of_air_transport(models.Model):
    title_page = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    histroy_content = RichTextField()
    profile_img = models.ImageField(blank=True,upload_to='pics')

    vision_title = models.CharField(max_length=200, blank=True)
    vision_description = RichTextField(blank=True)

    mission_title = models.CharField(max_length=200, blank=True)
    mission_description = RichTextField(blank=True)

    objective_title = models.CharField(max_length=200, blank=True)
    objective_description = RichTextField(blank=True)
    
    number_of_Human_Resource = models.IntegerField(blank=True)
    name_of_Human_Resource = models.CharField(max_length=200, blank=True)

    website_link = models.CharField(max_length=200, blank=True)
    facebook_link = models.CharField(max_length=200, blank=True)

    address_link = models.CharField(max_length=200, blank=True)

# DEPARTMENT OF IT & TELECOM
class department_of_it_telecom(models.Model):
    title_page = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    histroy_content = RichTextField()
    profile_img = models.ImageField(blank=True,upload_to='pics')

    vision_title = models.CharField(max_length=200, blank=True)
    vision_description = RichTextField(blank=True)

    mission_title = models.CharField(max_length=200, blank=True)
    mission_description = RichTextField(blank=True)

    objective_title = models.CharField(max_length=200, blank=True)
    objective_description = RichTextField(blank=True)
    
    number_of_Human_Resource = models.IntegerField(blank=True)
    name_of_Human_Resource = models.CharField(max_length=200, blank=True)

    website_link = models.CharField(max_length=200, blank=True)
    facebook_link = models.CharField(max_length=200, blank=True)

    address_link = models.CharField(max_length=200, blank=True)

# DEPARTMENT OF INFORMATION & MEDIA
class department_of_information_and_media(models.Model):
    title_page = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    histroy_content = RichTextField()
    profile_img = models.ImageField(blank=True,upload_to='pics')

    vision_title = models.CharField(max_length=200, blank=True)
    vision_description = RichTextField(blank=True)

    mission_title = models.CharField(max_length=200, blank=True)
    mission_description = RichTextField(blank=True)

    objective_title = models.CharField(max_length=200, blank=True)
    objective_description = RichTextField(blank=True)
    
    number_of_Human_Resource = models.IntegerField(blank=True)
    name_of_Human_Resource = models.CharField(max_length=200, blank=True)

    website_link = models.CharField(max_length=200, blank=True)
    facebook_link = models.CharField(max_length=200, blank=True)

    address_link = models.CharField(max_length=200, blank=True)

# ROAD SAFETY & TRANSPORT AUTHORITY
class road_safety_and_transport_authority(models.Model):
    title_page = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    histroy_content = RichTextField() 
    profile_img = models.ImageField(blank=True,upload_to='pics')

    vision_title = models.CharField(max_length=200, blank=True)
    vision_description = RichTextField(blank=True)

    mission_title = models.CharField(max_length=200, blank=True)
    mission_description = RichTextField(blank=True)

    objective_title = models.CharField(max_length=200, blank=True)
    objective_description = RichTextField(blank=True)
    
    number_of_Human_Resource = models.IntegerField(blank=True)
    name_of_Human_Resource = models.CharField(max_length=200, blank=True)

    website_link = models.CharField(max_length=200, blank=True)
    facebook_link = models.CharField(max_length=200, blank=True)

    address_link = models.CharField(max_length=200, blank=True)
