from django.contrib import admin

from .models import Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "type", "value", "is_active")
