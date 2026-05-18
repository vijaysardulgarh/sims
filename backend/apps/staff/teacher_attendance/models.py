from django.db import models

from apps.staff.staff.models import Staff
from apps.schools.models import School
from apps.core.models import SchoolBaseModel

class TeacherAttendance(SchoolBaseModel):

    teacher = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        limit_choices_to={
            "staff_role": "Teaching"
        }
    )

    date = models.DateField()

    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.teacher.name} - {self.date}"

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=["school", "teacher", "date"],
                name="unique_teacher_attendance_per_day"
            )
        ]

        indexes = [

            models.Index(
                fields=["school", "date"]
            ),

            models.Index(
                fields=["teacher", "date"]
            ),
        ]