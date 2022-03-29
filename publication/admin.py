from django.contrib import admin

from publication.models import policy, arts , rules_and_regulation, guideline, report , statistic

# Register your models here.
# POLICY
admin.site.register(policy)
admin.site.register(arts)
admin.site.register(rules_and_regulation)
admin.site.register(guideline)
admin.site.register(report)
admin.site.register(statistic)