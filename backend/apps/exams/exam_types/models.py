from django.db import models

from apps.core.models import SchoolBaseModel
class ExamType(SchoolBaseModel):

    CATEGORY_CHOICES = (
        ("school", "School"),
        ("college", "College"),
        ("competitive", "Competitive"),
        ("online", "Online"),
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.SlugField(
        max_length=50,
        unique=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="school"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_internal = models.BooleanField(
        default=False
    )

    is_practical = models.BooleanField(
        default=False
    )

    is_online = models.BooleanField(
        default=False
    )

    has_viva = models.BooleanField(
        default=False
    )

    has_assignment = models.BooleanField(
        default=False
    )

    default_max_marks = models.PositiveIntegerField(
        default=100
    )

    default_passing_marks = models.PositiveIntegerField(
        default=33
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Exam Type"

        verbose_name_plural = "Exam Types"

    def __str__(self):
        return self.name