from django.db import models

from apps.core.schools.models import School


class SystemSetting(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="settings"
    )

    key = models.CharField(
        max_length=100
    )

    value = models.TextField()

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.key