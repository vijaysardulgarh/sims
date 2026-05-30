from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.academics.streams.models import (
    Stream
)

from apps.academics.mediums.models import (
    Medium
)

from apps.infrastructure.classrooms.models import (
    Classroom
)

from apps.academics.classes.models import (
    Class
)

from apps.core.common.base.models import (
    SchoolBaseModel
)


class Section(
    SchoolBaseModel
):

    SUB_STREAM_CHOICES = [

        ("Medical", "Medical"),

        ("Non-Medical", "Non-Medical"),

        ("Vocational", "Vocational"),
    ]

    class_obj = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="sections",
        db_index=True
    )

    name = models.CharField(
        max_length=10,
        db_index=True
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

        super().clean()

        if self.name:

            self.name = (
                self.name.strip().upper()
            )

        if self.sub_stream and not self.stream:

            raise ValidationError(
                {
                    "sub_stream":
                    "Sub-stream requires a stream."
                }
            )

        if (
            self.class_obj
            and self.school
            and self.class_obj.school
            and self.class_obj.school != self.school
        ):

            raise ValidationError(
                {
                    "class_obj":
                    "Class must belong to the same school."
                }
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    class Meta:

        ordering = [
            "class_obj__display_order",
            "name"
        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "class_obj"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "name"
                ]
            ),
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "class_obj",
                    "name"
                ],
                name="unique_section_per_class_per_school"
            )
        ]

    def __str__(self):

        return (
            f"{self.class_obj.name} - "
            f"{self.name}"
        )