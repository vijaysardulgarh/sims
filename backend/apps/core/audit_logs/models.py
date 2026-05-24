from django.db import models

from apps.accounts.users.models import User


class AuditLog(models.Model):

    ACTION_CHOICES = [

        ("CREATE", "Create"),
        ("UPDATE", "Update"),
        ("DELETE", "Delete"),
        ("LOGIN", "Login"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    module = models.CharField(
        max_length=100
    )

    object_id = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user} - {self.action}"