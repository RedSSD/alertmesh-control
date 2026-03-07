from rest_framework import serializers

from .models import NotificationRule


class NotificationRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationRule
        fields = [
            "id",
            "severity",
            "channel",
            "recipients",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
