from django.db import models

from apps.exams.models import Exam
from apps.core.common.base.models import SchoolBaseModel

class ExamNotification(SchoolBaseModel):

    NOTIFICATION_TYPES = (
        ("exam", "Exam"),
        ("result", "Result"),
        ("admit_card", "Admit Card"),
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_TYPES
    )

    is_published = models.BooleanField(
        default=False
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title