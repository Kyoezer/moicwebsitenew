
# Register your models here.
from django.contrib import admin
from subscribe.models import subscribeUs, MailMessage

# Register your models here.


# class SubscribeFormAdmin(admin.ModelAdmin):
#     list_display = ('name','email_address')

admin.site.register(MailMessage),
admin.site.register(subscribeUs)
