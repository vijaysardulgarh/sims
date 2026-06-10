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


class SeatingPlan(
    SessionBaseModel
):

    exam = models.ForeignKey(

        Exam,

        on_delete=models.CASCADE,

        related_name="seating_plans",
    )

    student = models.ForeignKey(

        Student,

        on_delete=models.CASCADE,

        related_name="seating_plans",
    )

    room_number = models.CharField(
        max_length=50,
    )

    row_number = models.PositiveIntegerField()

    seat_number = models.CharField(
        max_length=20,
    )

    seat_label = models.CharField(

        max_length=50,

        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = (
            "seating_plans"
        )

        ordering = [

            "room_number",

            "row_number",

            "seat_number",
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

                name=(
                    "unique_exam_student_seat"
                ),
            ),

            models.UniqueConstraint(

                fields=[
                    "exam",
                    "room_number",
                    "seat_number",
                ],

                condition=models.Q(
                    is_deleted=False
                ),

                name=(
                    "unique_exam_room_seat"
                ),
            ),
        ]

    def __str__(self):

        return (
            f"{self.student} - "
            f"{self.room_number}"
        )