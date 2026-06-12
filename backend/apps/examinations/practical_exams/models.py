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

from apps.staff.profiles.models import (
    Staff,
)


class PracticalExam(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="practical_exams",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="practical_exams",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="practical_exams",
    )

    examiner = models.ForeignKey(

        Staff,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="conducted_practical_exams",
    )

    practical_date = models.DateField()

    practical_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    viva_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    lab_work_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    project_marks = models.DecimalField(

        max_digits=5,

        decimal_places=2,

        default=0,
    )

    total_marks = models.DecimalField(

        max_digits=6,

        decimal_places=2,

        default=0,
    )

    is_absent = models.BooleanField(
        default=False,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "practical_exams"
        )

        ordering = [
            "-practical_date",
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

                name=(
                    "unique_practical_exam"
                ),
            ),
        ]

    def save(
        self,
        *args,
        **kwargs
    ):

        self.total_marks = (

            self.practical_marks

            + self.viva_marks

            + self.lab_work_marks

            + self.project_marks
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