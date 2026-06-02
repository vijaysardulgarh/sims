# =============================================================================
# associations/roles/models/role.py
# =============================================================================

from django.db import models

from apps.core.common.base.models import SchoolBaseModel
from apps.associations.groups.models import Group


class Role(SchoolBaseModel):

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="roles",
        db_index=True
    )

    title = models.CharField(
        max_length=255
    )

    responsibilities = models.TextField(
        blank=True
    )

    class Meta:

        verbose_name = "Group Role"

        verbose_name_plural = "Group Roles"

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "group",
                    "title"
                ],
                name="unique_role_per_group"
            )
        ]

        ordering = [
            "title"
        ]

    def __str__(self):

        return (
            f"{self.title} - "
            f"{self.group.name}"
        )