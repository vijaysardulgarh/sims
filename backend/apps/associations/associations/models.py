# =============================================================================
# associations/models/association.py
# =============================================================================

from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from apps.documents.models import Document
from apps.core.common.base.models import SessionBaseModel


class Association(SessionBaseModel):

    # ============================================
    # CONSTANTS
    # ============================================

    TYPE_CLUB = "Club"
    TYPE_COMMITTEE = "Committee"
    TYPE_NODAL = "Nodal"

    STATUS_ACTIVE = "Active"
    STATUS_INACTIVE = "Inactive"
    STATUS_ARCHIVED = "Archived"

    # ============================================
    # CHOICES
    # ============================================

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

    # ============================================
    # BASIC INFORMATION
    # ============================================

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

    # ============================================
    # RELATIONS
    # ============================================

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

    # ============================================
    # CONTENT
    # ============================================

    description = models.TextField(
        blank=True,
        null=True
    )

    tasks = models.TextField(
        blank=True
    )

    # ============================================
    # WEBSITE
    # ============================================

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

    # ============================================
    # META
    # ============================================

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
                    "school",
                    "academic_session",
                    "slug"
                ],
                name=(
                    "unique_association_slug_"
                    "per_school_session"
                )
            ),

            models.UniqueConstraint(
                fields=[
                    "school",
                    "academic_session",
                    "name"
                ],
                name=(
                    "unique_association_name_"
                    "per_school_session"
                )
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

    # ============================================
    # VALIDATIONS
    # ============================================

    def clean(self):

        self.name = self.name.strip()

        if not self.name:

            raise ValidationError({
                "name":
                    "Association name cannot be empty"
            })

        if (
            self.chairperson and
            self.chairperson.school != self.school
        ):

            raise ValidationError({
                "chairperson":
                    "Chairperson must belong "
                    "to same school"
            })

    # ============================================
    # SAVE
    # ============================================

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.name)

            with transaction.atomic():

                slug = base_slug

                counter = 1

                while (

                    Association.objects

                    .select_for_update()

                    .filter(
                        school=self.school,
                        academic_session=(
                            self.academic_session
                        ),
                        slug=slug
                    )

                    .exclude(pk=self.pk)

                    .exists()
                ):

                    slug = (
                        f"{base_slug}-{counter}"
                    )

                    counter += 1

                self.slug = slug

        super().save(*args, **kwargs)

    # ============================================
    # STRING
    # ============================================

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.academic_session})"
        )