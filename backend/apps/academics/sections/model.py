from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.academics.streams.model import Stream
from apps.academics.mediums.model import Medium
from apps.academics.classrooms.model import Classroom
from apps.academics.classes.model import (
    Class
)


class Section(models.Model):

    SUB_STREAM_CHOICES = [

        ("Medical", "Medical"),

        ("Non-Medical", "Non-Medical"),

        ("Vocational", "Vocational"),
    ]

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="sections",
        db_index=True
    )

    class_obj = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="sections",
        db_index=True
    )

    name = models.CharField(
        max_length=10
    )

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections"
    )

    medium = models.ForeignKey(
        Medium,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections"
    )

    stream = models.ForeignKey(
        Stream,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections"
    )

    sub_stream = models.CharField(
        max_length=100,
        choices=SUB_STREAM_CHOICES,
        null=True,
        blank=True
    )

    def clean(self):

        if self.name:
            self.name = (
                self.name.strip().upper()
            )

        if self.sub_stream and not self.stream:

            raise ValidationError(
                "Sub-stream requires a stream"
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = [
            "class_obj__class_order",
            "name"
        ]

    def __str__(self):

        return self.name