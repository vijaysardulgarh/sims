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


class CompartmentExam(
    SessionBaseModel
):

    STATUS_CHOICES = [

        ("PENDING", "Pending"),

        ("REGISTERED", "Registered"),

        ("APPEARED", "Appeared"),

        ("PASSED", "Passed"),

        ("FAILED", "Failed"),
    ]

    original_exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="compartment_students",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="compartment_exams",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="compartment_exams",
    )

    registration_date = models.DateField()

    exam_date = models.DateField()

    marks_obtained = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        null=True,

        blank=True,
    )

    passing_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="PENDING",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "compartment_exams"
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
                    "unique_compartment_exam"
                ),
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.subject}"
        )