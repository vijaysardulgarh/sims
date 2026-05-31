from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Gallery(
    SchoolBaseModel
):

    title = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to="galleries/"
    )

    description = models.TextField(
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "galleries"

        verbose_name = "Gallery"

        verbose_name_plural = "Galleries"

        ordering = [
            "display_order",
            "title"
        ]

    def __str__(self):

        return self.title