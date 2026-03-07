from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Recipient
from .serializers import RecipientSerializer


class RecipientViewSet(viewsets.ModelViewSet):
    serializer_class = RecipientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Recipient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
