from django.db import models

from apps.core.common.base.models import AuditBaseModel


class Module(AuditBaseModel):

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    name = models.CharField(
        max_length=100,
    )

    slug = models.SlugField(
        unique=True,
    )

    path = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    is_menu = models.BooleanField(
        default=True,
    )

    def __str__(self):

        return self.name