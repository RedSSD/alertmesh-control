from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import NotificationRule
from .serializers import NotificationRuleSerializer


class NotificationRuleViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationRuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return NotificationRule.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
