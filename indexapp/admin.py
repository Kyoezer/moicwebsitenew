from pyexpat import model
from django.contrib import admin

from indexapp.models import  IpModel, post,  Category, Tag, profile, vacancie, event, PressRelease, information_and_download, tender
admin.site.site_header = "MOIC Admin"
admin.site.site_title = "MOIC Admin Portal"
admin.site.index_title = "Welcome to MOIC Dashboard "

class TagTublerInline(admin.TabularInline):
    model = Tag

class postAdmin(admin.ModelAdmin):
    inlines =[TagTublerInline]

# Register your models here.
admin.site.register(post, postAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(profile)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacancy_title', 'pub_date')


admin.site.register(vacancie, VacancyAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'category', 'status', 'pub_date')


admin.site.register(event, EventAdmin)
admin.site.register(PressRelease)
admin.site.register(information_and_download)


class TenderAdmin(admin.ModelAdmin):
    list_display = ('tender_id', 'tender_title', 'pub_date')


admin.site.register(tender, TenderAdmin)
admin.site.register(IpModel)

