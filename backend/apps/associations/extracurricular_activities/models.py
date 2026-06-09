# =============================================================================
# associations/extracurricular_activities/models.py
# =============================================================================

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from apps.core.common.base.models import SessionBaseModel


class ExtracurricularActivity(SessionBaseModel):

    CATEGORY_CHOICES = [
        ("Sports", "Sports"),
        ("Clubs", "Clubs"),
        ("Arts", "Arts"),
        ("Academic", "Academic"),
        ("Community Service", "Community Service"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    name = models.CharField(
        max_length=100,
        db_index=True
    )

    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        db_index=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
        db_index=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    coordinator = models.ForeignKey(
        "staff.Staff",
        on_delete=models.SET_NULL,
        null=True,
        related_name="coordinated_activities"
    )

    participants = models.ManyToManyField(
        "students.Student",
        related_name="participated_activities",
        blank=True
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    capacity = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1)]
    )

    priority = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Extracurricular Activity"
        verbose_name_plural = "Extracurricular Activities"

        ordering = [
            "priority",
            "name"
        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "category"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "status"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "start_date"
                ]
            ),
        ]

    def clean(self):

        if (
            self.coordinator and
            self.coordinator.school != self.school
        ):
            raise ValidationError(
                "Coordinator must belong to same school"
            )

        if (
            self.end_date and
            self.start_date and
            self.end_date < self.start_date
        ):
            raise ValidationError(
                "End date cannot be before start date"
            )

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.academic_session})"
        )