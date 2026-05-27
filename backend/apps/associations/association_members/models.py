# =============================================================================
# associations/models/association_member.py
# =============================================================================

from django.db import models
from django.core.exceptions import ValidationError

from apps.staff.profiles.models import Staff
from apps.associations.associations.models import (
    Association
)
from apps.core.common.base.models import SchoolBaseModel


class AssociationMember(SchoolBaseModel):

    association = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        related_name="members",
        db_index=True
    )

    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name="association_memberships",
        db_index=True
    )

    designation = models.CharField(max_length=50)

    email = models.EmailField(blank=True)

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    image = models.ImageField(
        upload_to="association_members/",
        blank=True
    )

    class Meta:
        verbose_name = "Association Member"
        verbose_name_plural = "Association Members"

        constraints = [
            models.UniqueConstraint(
                fields=["association", "staff"],
                name="unique_member"
            )
        ]

        ordering = [
            "designation",
            "staff__name"
        ]

    def clean(self):

        if self.staff.school != self.association.school:
            raise ValidationError(
                "Staff must belong to same school"
            )

    def __str__(self):

        return (
            f"{self.staff.name} "
            f"({self.designation}) - "
            f"{self.association.name}"
        )