from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)

from apps.exams.exams.models import (
    Exam,
)

from apps.students.students.models import (
    Student,
)


class AdmitCard(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="admit_cards",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="admit_cards",
    )

    roll_number = models.CharField(
        max_length=50,
    )

    issue_date = models.DateField()

    is_generated = models.BooleanField(
        default=False,
    )

    generated_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "admit_cards"

        ordering = [
            "-issue_date",
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

                name="unique_student_admit_card",
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.exam}"
        )