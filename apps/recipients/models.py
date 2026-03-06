from django.conf import settings
from django.db import models


class RecipientType(models.TextChoices):
    EMAIL = "email", "Email"
    SMS = "sms", "SMS"


class Recipient(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipients",
    )

    type = models.CharField(
        max_length=10,
        choices=RecipientType.choices,
    )

    value = models.CharField(max_length=255)

    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.type}:{self.value}"
