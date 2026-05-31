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

        max_length=50,

        unique=True
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

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        db_table = "classrooms"

        verbose_name = "Classroom"

        verbose_name_plural = "Classrooms"

        ordering = [
            "classroom_code"
        ]

    def __str__(self):

        return self.classroom_code