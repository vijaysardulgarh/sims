from django.db import models

from apps.core.common.base.models import SessionBaseModel
from apps.staff.profiles.models import Staff
from apps.timetables.period_definitions.models import PeriodDefinition


class TeacherAvailability(SessionBaseModel):

    # ============================================
    # DAY
    # ============================================

    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"
    SATURDAY = "SAT"
    SUNDAY = "SUN"

    DAY_CHOICES = [
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday"),
    ]

    # ============================================
    # TEACHER
    # ============================================

    teacher = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name="teacher_availabilities",
        limit_choices_to={
            "staff_role": "Teaching",
        },
    )

    # ============================================
    # DAY
    # ============================================

    day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
        db_index=True,
    )

    # ============================================
    # PERIOD
    # ============================================

    period = models.ForeignKey(
        PeriodDefinition,
        on_delete=models.CASCADE,
        related_name="teacher_availabilities",
    )

    # ============================================
    # AVAILABILITY
    # ============================================

    is_available = models.BooleanField(
        default=True,
    )

    # ============================================
    # REASON
    # ============================================

    reason = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    remarks = models.TextField(
        blank=True,
        default="",
    )

    # ============================================
    # META
    # ============================================

    class Meta:

        db_table = "tt_teacher_availabilities"

        verbose_name = "Teacher Availability"
        verbose_name_plural = "Teacher Availabilities"

        ordering = [
            "teacher__employee_id",
            "day",
            "period",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "academic_session",
                    "teacher",
                    "day",
                    "period",
                ],
                name="unique_teacher_availability",
            ),
        ]

        indexes = [
            models.Index(
                fields=[
                    "school",
                    "academic_session",
                ],
                name="teacher_av_school_session_idx",
            ),
            models.Index(
                fields=[
                    "teacher",
                    "day",
                ],
                name="teacher_av_teacher_day_idx",
            ),
            models.Index(
                fields=[
                    "teacher",
                    "is_available",
                ],
                name="teacher_av_status_idx",
            ),
        ]

    # ============================================
    # STRING
    # ============================================

    def __str__(self):
        return (
            f"{self.teacher.employee_id} - "
            f"{self.teacher.name} - "
            f"{self.get_day_display()} - "
            f"{self.period}"
        )

    # ============================================
    # DISPLAY PROPERTIES
    # ============================================

    @property
    def employee_id(self):
        return self.teacher.employee_id

    @property
    def teacher_name(self):
        return self.teacher.name