from django.contrib import admin

from contact.models import contactUs, ContactForm

# Register your models here.
admin.site.register(contactUs)
admin.site.register(ContactForm)
