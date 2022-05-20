from django.contrib import admin

from annual.models import select_annual_report, social_link, annual_performance_agreement

# Register your models here.
# admin.site.register(select_annual_report)
# admin.site.register(social_link)


class AnnualAdmin(admin.ModelAdmin):
    list_display = ('title', 'attachment')


admin.site.register(annual_performance_agreement, AnnualAdmin)
