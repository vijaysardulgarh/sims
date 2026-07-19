from django.db import models

from apps.staff.profiles.models import Staff
from apps.core.common.base.models import SchoolBaseModel


class TeacherAttendance(SchoolBaseModel):

    # ============================================
    # ATTENDANCE STATUS
    # ============================================

    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    LEAVE = "LEAVE"
    HALF_DAY = "HALF_DAY"
    OFFICIAL_DUTY = "OFFICIAL_DUTY"

    STATUS_CHOICES = [
        (PRESENT, "Present"),
        (ABSENT, "Absent"),
        (LEAVE, "Leave"),
        (HALF_DAY, "Half Day"),
        (OFFICIAL_DUTY, "Official Duty"),
    ]

    # ============================================
    # TEACHER
    # ============================================

    teacher = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name="teacher_attendance",
        limit_choices_to={
            "staff_role": "Teaching",
        },
    )

    # ============================================
    # ATTENDANCE DATE
    # ============================================

    date = models.DateField(
        db_index=True,
    )

    # ============================================
    # STATUS
    # ============================================

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PRESENT,
        db_index=True,
    )

    # ============================================
    # CHECK-IN / CHECK-OUT
    # ============================================

    check_in = models.TimeField(
        blank=True,
        null=True,
    )

    check_out = models.TimeField(
        blank=True,
        null=True,
    )

    # ============================================
    # REMARKS
    # ============================================

    remarks = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    # ============================================
    # META
    # ============================================

    class Meta:

        verbose_name = "Teacher Attendance"
        verbose_name_plural = "Teacher Attendance"

        ordering = [
            "-date",
            "teacher__employee_id",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "teacher",
                    "date",
                ],
                name="unique_teacher_attendance_per_day",
            ),
        ]

        indexes = [
            models.Index(
                fields=[
                    "school",
                    "date",
                ],
                name="teacher_att_school_date_idx",
            ),
            models.Index(
                fields=[
                    "teacher",
                    "date",
                ],
                name="teacher_att_teacher_date_idx",
            ),
            models.Index(
                fields=[
                    "school",
                    "status",
                ],
                name="teacher_att_school_status_idx",
            ),
        ]

    # ============================================
    # STRING
    # ============================================

    def __str__(self):
        return (
            f"{self.teacher.employee_id} - "
            f"{self.teacher.name} - "
            f"{self.date} ({self.status})"
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

    @property
    def post_type(self):
        return (
            self.teacher.post_type.name
            if self.teacher.post_type
            else ""
        )