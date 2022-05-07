from django.contrib import admin

from publication.models import policy, arts, rule, guideline, report, statistic, regulation

# Register your models here.
# POLICY


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title', 'attachment')


admin.site.register(policy, PolicyAdmin)


class ActsAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title', 'attachment')


admin.site.register(arts, ActsAdmin)


class RuleAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title', 'attachment')


admin.site.register(rule, RuleAdmin)


class GuidelineAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title', 'attachment')


admin.site.register(guideline, GuidelineAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title', 'attachment')


admin.site.register(report, ReportAdmin)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('SI_No', 'title', 'attachment')


admin.site.register(statistic, StatisticAdmin)
