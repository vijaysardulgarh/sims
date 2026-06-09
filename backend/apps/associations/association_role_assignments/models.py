# =============================================================================
# association_role_assignments/models.py
# =============================================================================

from django.db import models

from django.core.exceptions import ValidationError

from apps.associations.association_members.models import (
    AssociationMember
)

from apps.associations.association_roles.models import (
    AssociationRole
)

from apps.core.common.base.models import (
    SessionBaseModel
)


class AssociationRoleAssignment(
    SessionBaseModel
):

    member = models.ForeignKey(

        AssociationMember,

        on_delete=models.CASCADE,

        related_name="role_assignments",

        db_index=True,
    )

    role = models.ForeignKey(

        AssociationRole,

        on_delete=models.CASCADE,

        related_name="assigned_members",

        db_index=True,
    )

    class Meta:

        verbose_name = (
            "Association Role Assignment"
        )

        verbose_name_plural = (
            "Association Role Assignments"
        )

        constraints = [

            models.UniqueConstraint(

                fields=[
                    "academic_session",
                    "member",
                    "role",
                ],

                name="unique_member_role_assignment",
            ),

            models.UniqueConstraint(

                fields=[
                    "academic_session",
                    "role",
                ],

                name="unique_role_holder_per_session",
            ),
        ]

        ordering = [
            "role__title",
        ]

    def clean(self):

        if (

            self.member.association_id !=

            self.role.association_id

        ):

            raise ValidationError(

                "Role and Member must belong "
                "to the same association."
            )

    def __str__(self):

        return (

            f"{self.member.member_name}"

            f" - "

            f"{self.role.title}"
        )