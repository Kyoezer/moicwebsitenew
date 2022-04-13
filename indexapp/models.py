from distutils.command.upload import upload
from genericpath import exists
from sys import maxsize
from telnetlib import STATUS
from turtle import title
from unicodedata import category, name
from django.db import models
from django.forms import SlugField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime 


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )
    SECTION = (
        ('landimg', 'landimg'),
        ('Popular', 'Popular'),
        ('Recent', 'Recent'),
        ('latest', 'latest'),
    )
    post_name = models.CharField(max_length=100)
    post_img = models.ImageField(blank=True,upload_to='pics')
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=200)
    content = RichTextField()
    slug = models.SlugField(max_length=500, null= True, blank= True, unique= True)
    def __str__(self):
        return self.post_name

def create_slug(instance , new_slug=None):
     slug = slugify(instance.post_name)
     if new_slug is not None:
         slug = new_slug
     qs = post.objects.filter(slug=slug).order_by('-id')
     exists = qs.exists()
     if exists:
         new_slug = "%s-%s" % (slug, qs.first().id)
         return create_slug(instance, new_slug= new_slug)
     return slug
def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_reciver, post)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# profile models
class profile(models.Model):
    profile_img = models.ImageField(blank=True,upload_to='pics')
    profile_designation = models.CharField(max_length=200)
    profile_name = models.CharField(max_length=200)
    profile_bio = RichTextField()

# VACANCY
class vacancie(models.Model):
    vacancy_title = models.CharField(max_length=100)
    vacancy_img = models.ImageField(blank=True,upload_to='pics')
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    pub_date = models.DateTimeField('date published')
    vacancy_description = RichTextField()
    vacancy_file = models.FileField(blank = True, null = True, upload_to='files')

# event
class event(models.Model):
    event_title = models.CharField(max_length=100)
    event_img = models.ImageField(blank=True,upload_to='pics')
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    pub_date = models.DateTimeField('date published')
    event_description = RichTextField()
    event_file = models.FileField(blank = True, null = True, upload_to='files')


# TENDER
class tender(models.Model):
    tender_id = models.IntegerField(blank=True)
    tender_title = models.CharField(max_length=100)
    tender_img = models.ImageField(blank=True,upload_to='pics')
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    pub_date = models.DateTimeField('date published')
    tender_description = RichTextField()
    tender_file = models.FileField(blank = True, null = True, upload_to='files')


# PRESS RELEASE
class PressRelease(models.Model):
    press_title = models.CharField(max_length=100)
    press_img = models.ImageField(blank=True,upload_to='pics')
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    pub_date = models.DateTimeField('date published')
    press_description = RichTextField()

# INFORMATION & DOWNLOADS
class information_and_download(models.Model):
    title = models.CharField(max_length=100, blank=True)
    download_link = models.CharField(max_length=300, blank=True)
    info_description = RichTextField(blank=True)


class image_slider(models.Model):
    images = models.ImageField(blank=True, upload_to='pics')


   