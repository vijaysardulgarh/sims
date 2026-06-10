from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.rooms.models import (
    Room
)

class Classroom(
    SchoolBaseModel
):

    room = models.OneToOneField(
        Room,
        on_delete=models.CASCADE,
        related_name="classroom"
    )

    classroom_code = models.CharField(
        max_length=50
    )

    capacity = models.PositiveIntegerField(
        default=40
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    smart_classroom = models.BooleanField(
        default=False
    )

    air_conditioned = models.BooleanField(
        default=False
    )

    projector_available = models.BooleanField(
        default=False
    )

    whiteboard_available = models.BooleanField(
        default=True
    )

    internet_enabled = models.BooleanField(
        default=False
    )

    def clean(self):

        if (

            self.room

            and

            self.room.room_type
            !=
            "CLASSROOM"

        ):

            raise ValidationError(
                "Selected room is not a classroom."
            )

    def __str__(self):

        return (
            f"{self.classroom_code}"
            f" - "
            f"{self.room.room_name}"
        )

    class Meta:

        db_table = "classrooms"

        ordering = [
            "classroom_code"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "classroom_code"
                ],
                name=(
                    "unique_school_classroom_code"
                )
            )
        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "classroom_code"
                ]
            ),

            models.Index(
                fields=[
                    "is_active"
                ]
            ),

            models.Index(
                fields=[
                    "is_deleted"
                ]
            ),
        ]