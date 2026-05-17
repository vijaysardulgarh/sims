from django.db import models

from apps.core.schools.models import School


class Role(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):

        return self.name