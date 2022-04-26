from django.db import models


# Create your models here.
class contactUs(models.Model):
    top_title = models.CharField(max_length=100, blank=True)
    # Ministry of Information & Communications
    title = models.CharField(max_length=100, blank=True)
    pox_title = models.CharField(max_length=100, blank=True)
    # Thimphu : Bhutan
    address = models.CharField(max_length=100, blank=True)
    tel_phone = models.IntegerField(blank=True)
    mail = models.EmailField(blank=True)
    map = models.CharField(max_length=200, blank=True)


class ContactForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    message = models.CharField(max_length=2000)
