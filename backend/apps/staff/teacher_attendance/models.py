from django.db import models

from apps.staff.models import Staff


class TeacherAttendance(models.Model):

    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE
    )

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