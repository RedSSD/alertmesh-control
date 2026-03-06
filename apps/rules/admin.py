from django.contrib import admin

from .models import NotificationRule


@admin.register(NotificationRule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "severity", "channel")
