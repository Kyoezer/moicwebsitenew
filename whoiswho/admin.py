from django.contrib import admin

from whoiswho.models import top_title, office_of_minister, office_of_secretary, shortlink

# Register your models here.
admin.site.register(top_title)
admin.site.register(office_of_minister)
admin.site.register(office_of_secretary)
admin.site.register(shortlink)