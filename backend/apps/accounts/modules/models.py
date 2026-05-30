from django.db import models
from django.core.exceptions import ValidationError

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

    def clean(self):

        # Prevent self-parenting
        if self.parent_id and self.parent_id == self.id:
            raise ValidationError(
                "A module cannot be its own parent."
            )

        # Prevent circular relationships
        current = self.parent

        while current:

            if current.id == self.id:
                raise ValidationError(
                    "Circular parent relationship detected."
                )

            current = current.parent

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name