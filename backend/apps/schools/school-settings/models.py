from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


class SchoolSetting(
    SchoolBaseModel
):

    academic_year_format = models.CharField(
        max_length=50,
        default="2025-2026"
    )

    attendance_type = models.CharField(
        max_length=20,
        choices=[
            ("DAILY", "Daily"),
            ("PERIOD", "Period Wise"),
        ],
        default="DAILY"
    )

    grading_system = models.CharField(
        max_length=20,
        choices=[
            ("MARKS", "Marks"),
            ("GRADE", "Grade"),
            ("BOTH", "Both"),
        ],
        default="MARKS"
    )

    working_days_per_week = (
        models.PositiveIntegerField(
            default=6
        )
    )

    allow_online_admission = (
        models.BooleanField(
            default=True
        )
    )

    class Meta:

        db_table = (
            "school_settings"
        )

        constraints = [

            models.UniqueConstraint(
                fields=["school"],
                name=(
                    "unique_setting_per_school"
                )
            )
        ]

    def __str__(self):

        return (
            f"Settings - "
            f"{self.school.name}"
        )