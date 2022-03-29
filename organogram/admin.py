from django.contrib import admin

from organogram.models import top_title, human_resource, organogram, information_download

# Register your models here.
admin.site.register(top_title)
admin.site.register(human_resource)
admin.site.register(organogram)
admin.site.register(information_download)