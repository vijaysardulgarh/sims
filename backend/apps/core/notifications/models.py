from django.db import models

from apps.accounts.users.models import User


class Notification(models.Model):

    TYPE_CHOICES = [

        ("SMS", "SMS"),
        ("EMAIL", "Email"),
        ("SYSTEM", "System"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title