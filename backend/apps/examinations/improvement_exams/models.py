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

from apps.academics.subjects.models import (
    Subject,
)


class ImprovementExam(
    SessionBaseModel
):

    STATUS_CHOICES = [

        ("REGISTERED", "Registered"),

        ("APPEARED", "Appeared"),

        ("COMPLETED", "Completed"),

        ("APPROVED", "Approved"),

        ("REJECTED", "Rejected"),
    ]

    original_exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="improvement_exams",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="improvement_exams",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="improvement_exams",
    )

    registration_date = models.DateField()

    exam_date = models.DateField()

    original_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,
    )

    improvement_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        null=True,

        blank=True,
    )

    final_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        null=True,

        blank=True,
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="REGISTERED",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "improvement_exams"
        )

        ordering = [
            "-exam_date",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "student",
                    "original_exam",
                    "subject",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name=(
                    "unique_improvement_exam"
                ),
            ),
        ]

    def save(
        self,
        *args,
        **kwargs
    ):

        if self.improvement_marks:

            self.final_marks = max(

                self.original_marks,

                self.improvement_marks,
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.subject}"
        )