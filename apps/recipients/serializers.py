from rest_framework import serializers

from .models import Recipient


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            "id",
            "type",
            "value",
            "is_verified",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
