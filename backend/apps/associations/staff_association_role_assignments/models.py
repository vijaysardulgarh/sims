# =============================================================================
# staff_association_role_assignments/models.py
# =============================================================================

from django.db import models

from django.core.exceptions import (
    ValidationError
)

from apps.staff.profiles.models import (
    Staff
)

from apps.associations.association_roles.models import (
    AssociationRole
)

from apps.core.common.base.models import (
    SchoolBaseModel
)


class StaffAssociationRoleAssignment(
    SchoolBaseModel
):

    academic_session = models.ForeignKey(

        "academics.AcademicSession",

        on_delete=models.CASCADE,

        related_name=
        "staff_association_role_assignments",

        db_index=True
    )

    staff = models.ForeignKey(

        Staff,

        on_delete=models.CASCADE,

        related_name="association_roles",

        db_index=True
    )

    role = models.ForeignKey(

        AssociationRole,

        on_delete=models.CASCADE,

        related_name="assigned_staff",

        db_index=True
    )

    class Meta:

        verbose_name = (
            "Staff Role Assignment"
        )

        verbose_name_plural = (
            "Staff Role Assignments"
        )

        constraints = [

            models.UniqueConstraint(

                fields=[

                    "academic_session",

                    "staff",

                    "role"
                ],

                name=
                "unique_staff_role_session"
            )
        ]

    def clean(self):

        if (

            self.staff.school !=

            self.role.association.school
        ):

            raise ValidationError(

                "Staff must belong "
                "to same school"
            )

    def __str__(self):

        return (

            f"{self.staff.name} - "

            f"{self.role.title}"
        )