from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.academics.sections.model import Section
from apps.academics.class_subjects.model import (
    ClassSubject
)


class TeacherSubjectAssignment(
    models.Model
):

    teacher = models.ForeignKey(
        "staff.Staff",
        on_delete=models.CASCADE,
        related_name="subject_assignments",
        limit_choices_to={
            "staff_role": "Teaching"
        }
    )

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="subject_assignments"
    )

    class_subject = models.ForeignKey(
        ClassSubject,
        on_delete=models.CASCADE,
        related_name="teacher_assignments"
    )

    def clean(self):

        if (
            self.teacher.school !=
            self.section.school
        ):

            raise ValidationError(
                "Teacher and Section "
                "must belong to same school"
            )

        if (
            self.class_subject.school !=
            self.section.school
        ):

            raise ValidationError(
                "ClassSubject must belong "
                "to same school"
            )

        total = (
            TeacherSubjectAssignment.objects
            .filter(
                teacher=self.teacher
            )
            .exclude(pk=self.pk)
            .count()
        )

        if (
            total >=
            self.teacher.max_periods_per_week
        ):

            raise ValidationError(
                "Teacher exceeded max workload"
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.teacher.name}"
            f" → "
            f"{self.section}"
        )

    class Meta:

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "teacher",
                    "section",
                    "class_subject"
                ],

                name=(
                    "unique_teacher_"
                    "section_subject"
                )
            )
        ]

        indexes = [

            models.Index(
                fields=["section"]
            ),

            models.Index(
                fields=["teacher"]
            ),
        ]