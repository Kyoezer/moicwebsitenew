from django.contrib import admin

from whoiswho.models import *

# Register your models here.
# admin.site.register(top_title)


class MinisterOffice(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'phone_no', 'profile_img')


admin.site.register(office_of_minister, MinisterOffice)


class SecretaryOffice(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'phone_no', 'profile_img')


admin.site.register(office_of_secretary, SecretaryOffice)


class PPD(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(policy_planning_division, PPD)


class HRD(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(human_resource_division, HRD)


class ICTD(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(ict_division, ICTD)


class InternalAudit(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(internal_audit, InternalAudit)


class Administration(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(administration, Administration)


class FinanceDivision(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(finance_division, FinanceDivision)


class ProcurementSection(admin.ModelAdmin):
    list_display = ('title', 'name', 'mail_id', 'focal_person_for', 'phone_no', 'profile_img')


admin.site.register(procurement_section, ProcurementSection)
# admin.site.register(shortlink)
