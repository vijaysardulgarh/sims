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

from apps.examinations.result_generations.models import (
    ResultGeneration,
)


class ReportCard(
    SessionBaseModel
):

    result = models.OneToOneField(

        ResultGeneration,

        on_delete=models.CASCADE,

        related_name="report_card",
    )

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="report_cards",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="report_cards",
    )

    report_card_number = models.CharField(
        max_length=100,
    )

    issue_date = models.DateField()

    remarks = models.TextField(
        blank=True,
    )

    principal_remark = models.TextField(
        blank=True,
    )

    is_published = models.BooleanField(
        default=False,
    )

    published_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    class Meta:

        db_table = "report_cards"

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

                name="unique_report_card",
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.exam}"
        )