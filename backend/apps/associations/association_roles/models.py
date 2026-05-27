# =============================================================================
# associations/models/association_role.py
# =============================================================================

from django.db import models

from apps.core.common.base.models import SchoolBaseModel
from apps.associations.associations.models import Association


class AssociationRole(SchoolBaseModel):

    association = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        related_name="roles",
        db_index=True
    )

    title = models.CharField(max_length=255)

    responsibilities = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Association Role"
        verbose_name_plural = "Association Roles"

        constraints = [
            models.UniqueConstraint(
                fields=["association", "title"],
                name="unique_role_per_association"
            )
        ]

        ordering = ["title"]

    def __str__(self):

        return f"{self.title} - {self.association.name}"