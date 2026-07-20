from django.db import models

from apps.core.common.base.models import SessionBaseModel
from apps.staff.profiles.models import Staff


class TeacherPreference(SessionBaseModel):

    SHIFT_CHOICES = (
        ("MORNING", "Morning"),
        ("AFTERNOON", "Afternoon"),
    )

    teacher = models.OneToOneField(
        Staff,
        on_delete=models.CASCADE,
        related_name="teacher_preference",
    )

    # Period Preferences
    prefer_first_period = models.BooleanField(
        default=False,
        help_text="Prefer teaching in the first period.",
    )

    avoid_first_period = models.BooleanField(
        default=False,
        help_text="Avoid teaching in the first period.",
    )

    prefer_last_period = models.BooleanField(
        default=False,
        help_text="Prefer teaching in the last period.",
    )

    avoid_last_period = models.BooleanField(
        default=False,
        help_text="Avoid teaching in the last period.",
    )

    # Shift Preference
    preferred_shift = models.CharField(
        max_length=10,
        choices=SHIFT_CHOICES,
        blank=True,
        help_text="Preferred teaching session.",
    )

    # Gap Preference
    avoid_gaps_between_classes = models.BooleanField(
        default=False,
        help_text="Try to avoid idle periods between classes.",
    )

    maximum_free_gaps = models.PositiveSmallIntegerField(
        default=0,
        help_text="Maximum free periods allowed between teaching periods in a day.",
    )

    class Meta:

        db_table = "tt_teacher_preferences"

        verbose_name = "Teacher Preference"

        verbose_name_plural = "Teacher Preferences"

        ordering = [
            "teacher__name",
        ]

    def __str__(self):

        return self.teacher.name