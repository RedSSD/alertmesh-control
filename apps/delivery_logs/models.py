from django.conf import settings
from django.db import models


class DeliveryStatus(models.TextChoices):
    SENT = "sent", "Sent"
    FAILED = "failed", "Failed"


class DeliveryLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="delivery_logs",
    )

    recipient = models.CharField(max_length=255)

    channel = models.CharField(max_length=20)

    severity = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=DeliveryStatus.choices,
    )

    error_message = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.channel} -> {self.recipient} ({self.status})"
