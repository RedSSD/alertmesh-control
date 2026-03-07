from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ApiKey
from .serializers import ApiKeySerializer


class ApiKeyViewSet(viewsets.ModelViewSet):
    serializer_class = ApiKeySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ApiKey.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        raw_key = ApiKey.generate_key()

        serializer.save(
            user=self.request.user,
            key_hash=ApiKey.hash_key(raw_key),
        )

        serializer.instance.key = raw_key
