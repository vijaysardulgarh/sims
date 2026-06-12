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

from apps.accounts.users.models import User

class Revaluation(
    SessionBaseModel
):

    STATUS_CHOICES = [

        ("REQUESTED", "Requested"),

        ("UNDER_REVIEW", "Under Review"),

        ("APPROVED", "Approved"),

        ("REJECTED", "Rejected"),

        ("COMPLETED", "Completed"),
    ]

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="revaluations",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="revaluations",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="revaluations",
    )

    request_date = models.DateField()

    original_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,
    )

    revised_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        null=True,

        blank=True,
    )

    marks_difference = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="REQUESTED",
    )

    reason = models.TextField()

    reviewer_remarks = models.TextField(
        blank=True,
    )

    reviewed_by = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="reviewed_revaluations",
    )

    reviewed_at = models.DateTimeField(

        null=True,

        blank=True,
    )

    class Meta:

        db_table = (
            "revaluations"
        )

        ordering = [
            "-request_date",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "exam",
                    "student",
                    "subject",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_revaluation_request",
            ),
        ]

    def save(
        self,
        *args,
        **kwargs
    ):

        if self.revised_marks is not None:

            self.marks_difference = (

                self.revised_marks
                -
                self.original_marks
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