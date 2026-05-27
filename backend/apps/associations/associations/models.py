# =============================================================================
# associations/models/association.py
# =============================================================================

from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from apps.documents.models import Document
from apps.core.common.base.models import SchoolBaseModel


class Association(SchoolBaseModel):

    TYPE_CHOICES = [
        ("Club", "Club"),
        ("Committee", "Committee"),
        ("Nodal", "Nodal"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Archived", "Archived"),
    ]

    academic_session = models.ForeignKey(
        "academics.AcademicSession",
        on_delete=models.CASCADE,
        related_name="associations",
        db_index=True
    )

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
        default="Active",
        db_index=True
    )

    chairperson = models.ForeignKey(
        "staff.Staff",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="chaired_associations"
    )

    tasks = models.TextField(blank=True)

    documents = models.ManyToManyField(
        Document,
        related_name="associations",
        blank=True
    )

    show_on_website = models.BooleanField(default=True)

    description = models.TextField(
        blank=True,
        null=True
    )

    slug = models.SlugField(
        blank=True,
        db_index=True
    )

    priority = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Association"
        verbose_name_plural = "Associations"

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "school",
                    "academic_session",
                    "slug"
                ],
                name="unique_association_slug_per_school_session"
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "academic_session",
                    "name"
                ],
                name="unique_association_name_per_school_session"
            ),
        ]

        indexes = [

            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "association_type"
                ]
            ),

            models.Index(
                fields=[
                    "school",
                    "academic_session",
                    "status"
                ]
            ),
        ]

        ordering = [
            "priority",
            "name"
        ]

    def clean(self):

        if (
            self.chairperson and
            self.chairperson.school != self.school
        ):
            raise ValidationError(
                "Chairperson must belong to same school"
            )

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.name)

            with transaction.atomic():

                slug = base_slug
                counter = 1

                while Association.objects.select_for_update().filter(
                    school=self.school,
                    academic_session=self.academic_session,
                    slug=slug
                ).exclude(pk=self.pk).exists():

                    slug = f"{base_slug}-{counter}"
                    counter += 1

                self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.academic_session})"
        )