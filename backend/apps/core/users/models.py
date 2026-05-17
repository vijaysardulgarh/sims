from django.db import models

from django.contrib.auth.models import (
    AbstractUser
)

from apps.core.schools.models import School


class User(AbstractUser):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    profile_photo = models.ImageField(
        upload_to="users/photos/",
        blank=True,
        null=True
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.username