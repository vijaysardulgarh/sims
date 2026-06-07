from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.infrastructure.rooms.models import (
    Room
)

from apps.infrastructure.floors.models import (
    Floor
)


# ==========================================
# CLASSROOM MODEL
# ==========================================

class Classroom(
    SchoolBaseModel
):

    # ======================================
    # ROOM LINK
    # ======================================

    room = models.OneToOneField(

        Room,

        on_delete=models.CASCADE,

        related_name="classroom"
    )

    floor = models.ForeignKey(

        Floor,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="classrooms"
    )

    # ======================================
    # BASIC INFO
    # ======================================

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

    # ======================================
    # FACILITIES
    # ======================================

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

    # ======================================
    # STRING
    # ======================================

    def __str__(
        self
    ):

        return (
            f"{self.classroom_code}"
        )

    # ======================================
    # META
    # ======================================

    class Meta:

        db_table = "classrooms"

        verbose_name = (
            "Classroom"
        )

        verbose_name_plural = (
            "Classrooms"
        )

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
            ),

            models.UniqueConstraint(

                fields=[

                    "school",

                    "room"
                ],

                name=(
                    "unique_school_classroom_room"
                )
            ),
        ]

        indexes = [

            models.Index(
                fields=[
                    "school"
                ]
            ),

            models.Index(
                fields=[
                    "classroom_code"
                ]
            ),

            models.Index(
                fields=[
                    "floor"
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