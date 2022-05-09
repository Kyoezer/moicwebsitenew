from django.contrib import admin
from contact.models import contactUs, ContactForm

# Register your models here.
# admin.site.register(contactUs)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address')


admin.site.register(ContactForm, ContactFormAdmin)
