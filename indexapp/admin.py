from pyexpat import model
from django.contrib import admin

from indexapp.models import   post,  Category, Tag, profile, vacancie, event, PressRelease, information_and_download
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
admin.site.register(vacancie)
admin.site.register(event)
admin.site.register(PressRelease)
admin.site.register(information_and_download)


