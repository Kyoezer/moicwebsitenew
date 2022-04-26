from django.contrib import admin

from publication.models import policy, arts, rule, guideline, report, statistic, regulation

# Register your models here.
# POLICY
admin.site.register(policy)
admin.site.register(arts)
admin.site.register(rule)
admin.site.register(regulation)
admin.site.register(guideline)
admin.site.register(report)
admin.site.register(statistic)
