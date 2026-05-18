from django.db import models
from apps.core.models import SchoolBaseModel

class Class(
    SchoolBaseModel
):

    name = models.CharField(
        max_length=50
    )

    class_order = models.PositiveIntegerField(
        default=0
    )

    def clean(self):

        if self.name:

            self.name = (
                self.name.strip().upper()
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = [
            "class_order",
            "name"
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