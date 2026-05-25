from django.db import models

from apps.core.common.base.models import AuditBaseModel


class Module(AuditBaseModel):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:

        db_table = "auth_modules"

        ordering = [
            "name",
        ]

    def __str__(self):

        return self.name