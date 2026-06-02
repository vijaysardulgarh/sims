from django.db import models
from django.db.models import Max

from apps.core.common.base.models import SchoolBaseModel


class Class(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=50
    )

    display_order = models.PositiveIntegerField(
        default=0,
        blank=True
    )

    def clean(self):

        super().clean()

        if self.name:

            self.name = (
                self.name.strip().upper()
            )

    def save(self, *args, **kwargs):

        # Auto-generate display order only on create
        if self._state.adding and not self.display_order:

            max_order = (
                Class.objects
                .filter(
                    school=self.school
                )
                .aggregate(
                    Max("display_order")
                )
                .get(
                    "display_order__max"
                )
                or 0
            )

            self.display_order = (
                max_order + 1
            )

        self.full_clean()

        super().save(
            *args,
            **kwargs
        )

    class Meta:

        ordering = [
            "display_order",
            "name"
        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "display_order"
                ]
            )

        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="unique_class_per_school"
            )

        ]

    def __str__(self):

        return self.name