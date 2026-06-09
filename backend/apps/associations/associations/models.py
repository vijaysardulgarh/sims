# =============================================================================
# associations/models/association.py
# =============================================================================

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from apps.documents.models import Document
from apps.core.common.base.models import SessionBaseModel


class Association(SessionBaseModel):

    TYPE_CLUB = "Club"
    TYPE_COMMITTEE = "Committee"
    TYPE_NODAL = "Nodal"

    STATUS_ACTIVE = "Active"
    STATUS_INACTIVE = "Inactive"
    STATUS_ARCHIVED = "Archived"

    TYPE_CHOICES = [
        (TYPE_CLUB, "Club"),
        (TYPE_COMMITTEE, "Committee"),
        (TYPE_NODAL, "Nodal"),
    ]

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    association_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        db_index=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
        db_index=True
    )

    chairperson = models.ForeignKey(
        "staff.Staff",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="chaired_associations"
    )

    documents = models.ManyToManyField(
        Document,
        related_name="associations",
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    objectives = models.TextField(
        blank=True
    )

    show_on_website = models.BooleanField(
        default=True
    )

    slug = models.SlugField(
        max_length=255,
        blank=True,
        db_index=True
    )

    priority = models.PositiveIntegerField(
        default=0,
        db_index=True
    )

    class Meta:

        verbose_name = "Association"

        verbose_name_plural = "Associations"

        ordering = [
            "-priority",
            "name"
        ]

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "academic_session",
                    "school",
                    "name"
                ],
                name="unique_association_session"
            )

        ]

        indexes = [

            models.Index(
                fields=[
                    "academic_session",
                    "association_type"
                ]
            ),

            models.Index(
                fields=[
                    "academic_session",
                    "status"
                ]
            )

        ]

    def clean(self):

        if self.priority < 0:

            raise ValidationError(
                "Priority cannot be negative."
            )

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(
                f"{self.name}-{self.academic_session}"
            )

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.academic_session})"
        )