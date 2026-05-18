from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.academics.classes.models import Class
from apps.academics.streams.models import Stream
from apps.academics.subjects.models import Subject
from apps.core.models import SchoolBaseModel

class ClassSubject(SchoolBaseModel):

    class_obj = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    stream = models.ForeignKey(
        Stream,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stream_subjects",
        db_index=True
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True
    )

    sub_stream = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    theory_periods_per_week = (
        models.PositiveIntegerField(
            default=0
        )
    )

    practical_periods_per_week = (
        models.PositiveIntegerField(
            default=0
        )
    )

    periods_per_week = (
        models.PositiveIntegerField(
            default=0
        )
    )

    is_optional = models.BooleanField(
        default=False
    )

    has_lab = models.BooleanField(
        default=False
    )

    is_shared = models.BooleanField(
        default=False
    )

    class Meta:

        db_table = "class_subjects"

        ordering = [
            "class_obj__class_order",
            "subject__name"
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "school",
                    "class_obj",
                    "stream",
                    "subject",
                    "sub_stream"
                ],

                name="unique_class_subject"
            )
        ]

    def clean(self):

        if (
            self.theory_periods_per_week < 0 or
            self.practical_periods_per_week < 0
        ):

            raise ValidationError(
                "Periods cannot be negative."
            )

        total = (

            self.theory_periods_per_week +

            self.practical_periods_per_week
        )

        if total <= 0:

            raise ValidationError(
                "Total periods must "
                "be greater than 0."
            )

        senior_classes = [

            "11TH",

            "12TH",

            "ELEVENTH",

            "TWELFTH"
        ]

        if self.stream and (

            self.class_obj.name.upper()

            not in senior_classes
        ):

            raise ValidationError({

                "stream":
                "Streams are allowed only "
                "for senior classes."
            })

    def save(self, *args, **kwargs):

        self.periods_per_week = (

            self.theory_periods_per_week +

            self.practical_periods_per_week
        )

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        parts = [

            self.subject.name,

            f"({self.class_obj})"
        ]

        if self.stream:

            parts.append(
                self.stream.name
            )

        if self.sub_stream:

            parts.append(
                self.sub_stream
            )

        return " - ".join(parts)