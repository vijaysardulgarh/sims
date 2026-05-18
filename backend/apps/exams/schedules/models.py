from django.db import models

from apps.exams.models import Exam


class ExamSchedule(models.Model):

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    class_name = models.CharField(
        max_length=100
    )

    section = models.CharField(
        max_length=20
    )

    subject = models.CharField(
        max_length=100
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    room = models.CharField(
        max_length=100
    )

    invigilator = models.CharField(
        max_length=100
    )

    max_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100
    )

    passing_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=33
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.exam.name} - {self.subject}"