from rest_framework import serializers

from .models import ApiKey


class ApiKeySerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)

    class Meta:
        model = ApiKey
        fields = [
            "id",
            "name",
            "key",
            "is_active",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "key",
            "created_at",
        ]
