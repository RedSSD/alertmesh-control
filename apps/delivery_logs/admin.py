from django.contrib import admin

from .models import DeliveryLog


@admin.register(DeliveryLog)
class DeliveryLogAdmin(admin.ModelAdmin):
    list_display = ("id", "recipient", "channel", "status", "created_at")
