from django.db import models

from django.core.exceptions import (
    ValidationError
)

from django.db.models import Q


# =========================================
# DAY
# =========================================

class Day(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        db_index=True
    )

    name = models.CharField(max_length=20)

    sequence = models.PositiveIntegerField()

    class Meta:

        ordering = ["sequence"]

    def __str__(self):

        return self.name


# =========================================
# TIMETABLE SLOT
# =========================================

class TimetableSlot(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        db_index=True
    )

    day = models.ForeignKey(
        "Day",
        on_delete=models.CASCADE,
        db_index=True
    )

    sequence_number = (
        models.PositiveIntegerField()
    )

    period_number = (
        models.PositiveIntegerField(
            null=True,
            blank=True
        )
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_break = models.BooleanField(
        default=False
    )

    is_assembly = models.BooleanField(
        default=False
    )

    is_special_event = models.BooleanField(
        default=False
    )

    def clean(self):

        if self.start_time >= self.end_time:

            raise ValidationError(
                "End time must be greater."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.day.name}"
            f" ({self.period_number})"
        )


# =========================================
# TIMETABLE
# =========================================

class Timetable(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    teacher_subject_assignment = (
        models.ForeignKey(

            "staff.TeacherSubjectAssignment",

            on_delete=models.CASCADE,

            related_name="timetable_entries",

            db_index=True
        )
    )

    slot = models.ForeignKey(
        "TimetableSlot",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    classroom = models.ForeignKey(
        "Classroom",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    substitute_teacher = (
        models.ForeignKey(

            "staff.Staff",

            on_delete=models.SET_NULL,

            null=True,

            blank=True,

            related_name="substitute_entries",
        )
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "slot__day",
            "slot__sequence_number"
        ]

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    @property
    def teacher(self):

        return (
            self.teacher_subject_assignment.teacher
        )

    @property
    def section(self):

        return (
            self.teacher_subject_assignment.section
        )

    @property
    def class_subject(self):

        return (
            self.teacher_subject_assignment.class_subject
        )