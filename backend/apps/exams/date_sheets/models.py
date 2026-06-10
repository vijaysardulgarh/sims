from django.db import models

from apps.core.models.base_models import (
    SessionBaseModel,
)

from apps.exams.exams.models import (
    Exam,
)

from apps.academics.classes.models import (
    Class,
)

from apps.academics.sections.models import (
    Section,
)

from apps.academics.subjects.models import (
    Subject,
)

from apps.staff.employees.models import (
    Employee,
)


class DateSheet(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="date_sheets",
    )

    class_obj = models.ForeignKey(

        Class,

        on_delete=models.PROTECT,

        related_name="exam_schedules",
    )

    section = models.ForeignKey(

        Section,

        on_delete=models.PROTECT,

        related_name="exam_schedules",
    )

    subject = models.ForeignKey(

        Subject,

        on_delete=models.PROTECT,

        related_name="exam_schedules",
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    room_number = models.CharField(

        max_length=50,

        blank=True,
    )

    invigilator = models.ForeignKey(

        Employee,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="invigilated_exams",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "date_sheets"

        ordering = [
            "exam_date",
            "start_time",
        ]

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "exam",
                    "class_obj",
                    "section",
                    "subject",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name="unique_exam_subject_schedule",
            ),
        ]

    def __str__(self):

        return (
            f"{self.exam} - "
            f"{self.subject}"
        )