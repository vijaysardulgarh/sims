from django.db import models

from apps.core.schools.models import School


class Branch(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="branches"
    )

    name = models.CharField(
        max_length=255
    )

    code = models.CharField(
        max_length=50
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
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

        return self.name