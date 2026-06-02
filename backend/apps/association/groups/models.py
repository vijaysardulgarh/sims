# =============================================================================
# groups/models/group.py
# =============================================================================

from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from apps.documents.models import Document
from apps.core.common.base.models import SessionBaseModel


class Group(SessionBaseModel):

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

    group_type = models.CharField(
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
        related_name="chaired_groups"
    )

    documents = models.ManyToManyField(
        Document,
        related_name="groups",
        blank=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    tasks = models.TextField(
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

        verbose_name = "Group"

        verbose_name_plural = "Groups"

        ordering = [
            "-priority",
            "name"
        ]

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.academic_session})"
        )