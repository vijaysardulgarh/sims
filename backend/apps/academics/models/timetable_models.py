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
        related_name="days",
        db_index=True
    )

    name = models.CharField(
        max_length=20
    )

    sequence = models.PositiveIntegerField()

    class Meta:

        ordering = ["sequence"]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "name"
                ],
                name="unique_day_per_school"
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "sequence"
                ],
                name="unique_day_sequence_per_school"
            )
        ]

    def save(self, *args, **kwargs):

        if self.name:
            self.name = self.name.strip().title()

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name


# =========================================
# TIMETABLE SLOT
# =========================================

class TimetableSlot(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name="timetable_slots",
        db_index=True
    )

    day = models.ForeignKey(
        "academics.Day",
        on_delete=models.CASCADE,
        related_name="slots",
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

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:

        ordering = [
            "day__sequence",
            "sequence_number"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "day",
                    "sequence_number"
                ],
                name="unique_slot_sequence_per_day"
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "day",
                    "period_number"
                ],
                condition=Q(
                    period_number__isnull=False
                ),
                name="unique_period_per_day"
            )
        ]

    def clean(self):

        if self.start_time >= self.end_time:

            raise ValidationError(
                "End time must be greater than start time."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        if self.period_number:
            return (
                f"{self.day.name}"
                f" - Period {self.period_number}"
            )

        return (
            f"{self.day.name}"
            f" - Special Slot"
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

            "academics.TeacherSubjectAssignment",

            on_delete=models.CASCADE,

            related_name="timetable_entries",

            db_index=True
        )
    )

    slot = models.ForeignKey(
        "academics.TimetableSlot",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    classroom = models.ForeignKey(
        "academics.Classroom",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="timetable_entries"
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

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "slot__day__sequence",
            "slot__sequence_number"
        ]

        constraints = [

            # One section per slot
            models.UniqueConstraint(
                fields=[
                    "slot",
                    "teacher_subject_assignment"
                ],
                name="unique_assignment_per_slot"
            )
        ]

    def clean(self):

        teacher = (
            self.teacher_subject_assignment.teacher
        )

        section = (
            self.teacher_subject_assignment.section
        )

        # ---------------------------------
        # Prevent teacher collision
        # ---------------------------------

        teacher_conflict = Timetable.objects.exclude(
            pk=self.pk
        ).filter(
            slot=self.slot,
            teacher_subject_assignment__teacher=teacher
        )

        if teacher_conflict.exists():

            raise ValidationError(
                "Teacher already assigned in this slot."
            )

        # ---------------------------------
        # Prevent section collision
        # ---------------------------------

        section_conflict = Timetable.objects.exclude(
            pk=self.pk
        ).filter(
            slot=self.slot,
            teacher_subject_assignment__section=section
        )

        if section_conflict.exists():

            raise ValidationError(
                "Section already has timetable in this slot."
            )

        # ---------------------------------
        # Prevent classroom collision
        # ---------------------------------

        if self.classroom:

            classroom_conflict = Timetable.objects.exclude(
                pk=self.pk
            ).filter(
                slot=self.slot,
                classroom=self.classroom
            )

            if classroom_conflict.exists():

                raise ValidationError(
                    "Classroom already occupied."
                )

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

    def __str__(self):

        return (
            f"{self.teacher} - "
            f"{self.section} - "
            f"{self.slot}"
        )