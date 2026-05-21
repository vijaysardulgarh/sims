from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.academics.timetable_slots.models import (
    TimetableSlot
)

from apps.academics.teacher_subject_assignments.models import (
    TeacherSubjectAssignment
)

from apps.academics.classrooms.models import (
    Classroom
)

from apps.staff.profiles.models import Staff

from apps.schools.models import School

from apps.core.models import SchoolBaseModel

class Timetable(SchoolBaseModel):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    teacher_subject_assignment = (
        models.ForeignKey(

            TeacherSubjectAssignment,

            on_delete=models.CASCADE,

            related_name="timetable_entries",

            db_index=True
        )
    )

    slot = models.ForeignKey(
        TimetableSlot,
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True
    )

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="timetable_entries"
    )

    substitute_teacher = (
        models.ForeignKey(

            Staff,

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
            "slot__period_number"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "slot",
                    "teacher_subject_assignment"
                ],

                name="unique_assignment_per_slot"
            )
        ]

        indexes = [

            models.Index(
                fields=["slot"]
            ),

            models.Index(
                fields=[
                    "school",
                    "slot"
                ]
            ),
        ]

    def clean(self):

        teacher = (
            self.teacher_subject_assignment
            .teacher
        )

        section = (
            self.teacher_subject_assignment
            .section
        )

        teacher_conflict = (

            Timetable.objects

            .exclude(
                pk=self.pk
            )

            .filter(
                slot=self.slot,
                teacher_subject_assignment__teacher=teacher
            )
        )

        if teacher_conflict.exists():

            raise ValidationError({
                "teacher_subject_assignment":
                    (
                        "Teacher already assigned "
                        "in this slot."
                    )
            })

        section_conflict = (

            Timetable.objects

            .exclude(
                pk=self.pk
            )

            .filter(
                slot=self.slot,
                teacher_subject_assignment__section=section
            )
        )

        if section_conflict.exists():

            raise ValidationError({
                "slot":
                    (
                        "Section already has "
                        "timetable in this slot."
                    )
            })

        if self.classroom:

            classroom_conflict = (

                Timetable.objects

                .exclude(
                    pk=self.pk
                )

                .filter(
                    slot=self.slot,
                    classroom=self.classroom
                )
            )

            if classroom_conflict.exists():

                raise ValidationError({
                    "classroom":
                        "Classroom already occupied."
                })

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    @property
    def teacher(self):

        return (
            self.teacher_subject_assignment
            .teacher
        )

    @property
    def section(self):

        return (
            self.teacher_subject_assignment
            .section
        )

    @property
    def class_subject(self):

        return (
            self.teacher_subject_assignment
            .class_subject
        )

    def __str__(self):

        return (
            f"{self.teacher}"
            f" - "
            f"{self.section}"
            f" - "
            f"{self.slot}"
        )