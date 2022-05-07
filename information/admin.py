from django.contrib import admin
from .models import *

# Register your models here.


class HrAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title')


admin.site.register(hrdecisions, HrAdmin)
