from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# STAFF PROFILE OF THE MINISTRY
class top_title(models.Model):
    top_title = models.CharField(max_length=300)


# OFFICE OF THE MINISTER
class office_of_minister(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True, null=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

# OFFICE OF THE SECRETARY
class office_of_secretary(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

# PPD
class policy_planning_division(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

    # HRD
class human_resource_division(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

    # ICT
class ict_division(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

     # IA
class internal_audit(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

    #adm
class administration(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

    #finance_divison
class finance_division(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True,upload_to='pics')

    #procurement_section
class procurement_section(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail_id = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True)
    profile_img = models.ImageField(blank=True, upload_to='pics')


# short link
class shortlink(models.Model):
    title = models.CharField(max_length=200)
    shortlink_description = RichTextField(blank=True)