from django.conf import settings
from django.db import models


class Severity(models.TextChoices):
    INFO = "info", "Info"
    WARNING = "warning", "Warning"
    CRITICAL = "critical", "Critical"


class Channel(models.TextChoices):
    EMAIL = "email", "Email"
    SMS = "sms", "SMS"


class NotificationRule(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rules",
    )

    severity = models.CharField(
        max_length=20,
        choices=Severity.choices,
    )

    channel = models.CharField(
        max_length=20,
        choices=Channel.choices,
    )

    recipients: models.ManyToManyField = models.ManyToManyField(
        "recipients.Recipient",
        related_name="rules",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.id} {self.severity} -> {self.channel}"
