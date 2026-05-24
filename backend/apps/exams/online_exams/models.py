from django.db import models

from apps.exams.models import Exam
from apps.core.common.base.models import SchoolBaseModel

class OnlineExam(SchoolBaseModel):

    exam = models.OneToOneField(
        Exam,
        on_delete=models.CASCADE
    )

    duration_minutes = models.PositiveIntegerField()

    total_questions = models.PositiveIntegerField()

    negative_marking = models.BooleanField(
        default=False
    )

    random_questions = models.BooleanField(
        default=True
    )

    start_datetime = models.DateTimeField()

    end_datetime = models.DateTimeField()

    instructions = models.TextField()

    def __str__(self):
        return self.exam.name