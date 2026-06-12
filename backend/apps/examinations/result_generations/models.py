from django.db import models

from apps.core.common.base.models import (
    SessionBaseModel,
)

from apps.examinations.exams.models import (
    Exam,
)

from apps.students.profiles.models import (
    Student,
)


class ResultGeneration(
    SessionBaseModel
):

    RESULT_STATUS_CHOICES = [

        ("PASS", "Pass"),

        ("FAIL", "Fail"),

        ("COMPARTMENT", "Compartment"),
    ]

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="results",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="results",
    )

    total_marks = models.DecimalField(

        max_digits=8,

        decimal_places=2,
    )

    obtained_marks = models.DecimalField(

        max_digits=8,

        decimal_places=2,
    )

    percentage = models.DecimalField(

        max_digits=6,

        decimal_places=2,
    )

    overall_grade = models.CharField(
        max_length=20,
    )

    grade_point = models.DecimalField(

        max_digits=4,

        decimal_places=2,

        null=True,

        blank=True,
    )

    class_rank = models.PositiveIntegerField(

        null=True,

        blank=True,
    )

    section_rank = models.PositiveIntegerField(

        null=True,

        blank=True,
    )

    school_rank = models.PositiveIntegerField(

        null=True,

        blank=True,
    )

    result_status = models.CharField(

        max_length=20,

        choices=RESULT_STATUS_CHOICES,
    )

    is_published = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "result_generations"
        )

        ordering = [
            "-percentage",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "exam",
                    "student",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_exam_result",
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.exam}"
        )