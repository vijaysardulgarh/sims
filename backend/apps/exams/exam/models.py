from django.db import models
from apps.core.models import SchoolBaseModel

class Exam(SchoolBaseModel):

    EXAM_MODES = (
        ("offline", "Offline"),
        ("online", "Online"),
        ("hybrid", "Hybrid"),
    )

    GRADING_SYSTEMS = (
        ("marks", "Marks"),
        ("percentage", "Percentage"),
        ("grade", "Grade"),
        ("gpa", "GPA"),
        ("cgpa", "CGPA"),
    )

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("published", "Published"),
    )

    name = models.CharField(
        max_length=255
    )

    exam_type = models.CharField(
        max_length=100
    )

    exam_mode = models.CharField(
        max_length=20,
        choices=EXAM_MODES,
        default="offline"
    )

    grading_system = models.CharField(
        max_length=20,
        choices=GRADING_SYSTEMS,
        default="marks"
    )

    academic_year = models.CharField(
        max_length=20
    )

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name