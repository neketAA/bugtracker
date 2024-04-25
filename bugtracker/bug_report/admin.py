from django.contrib import admin
from .models import User_report


def get_display_value(value, choices):
    for choice in choices:
        if choice[0] == value:
            return choice[1]
    return None

class UserReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_priority', 'display_seriousness', 'display_status')

    def display_priority(self, obj):
        return get_display_value(obj.priority, User_report.PRIORITY_CHOICES)

    def display_seriousness(self, obj):
        return get_display_value(obj.seriousness, User_report.SERIOUSNESS_CHOICES)

    def display_status(self, obj):
        return get_display_value(obj.status, User_report.STATUS_CHOICES)

admin.site.register(User_report, UserReportAdmin)
