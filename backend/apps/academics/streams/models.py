from django.db import models

from apps.core.models import SchoolBaseModel

class Stream(
    SchoolBaseModel
):


    name = models.CharField(
        max_length=100,
        db_index=True
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
            "name"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="unique_stream_per_school"
            )
        ]

    def __str__(self):

        return self.name