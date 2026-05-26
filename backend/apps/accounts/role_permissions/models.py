from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)


from apps.accounts.roles.models import (
    Role
)

from apps.accounts.permissions.models import (
    Permission
)


# ==========================================
# ROLE PERMISSION MODEL
# ==========================================

class RolePermission(
    SchoolBaseModel
):

    role = models.ForeignKey(

        Role,

        on_delete=models.CASCADE,

        related_name="role_permissions"
    )

    permission = models.ForeignKey(

        Permission,

        on_delete=models.CASCADE,

        related_name="role_permissions"
    )

    class Meta:

        unique_together = (

            "school",

            "role",

            "permission"
        )

        ordering = [
            "role__name"
        ]

    def __str__(self):

        return (
            f"{self.role.name} - "
            f"{self.permission.code}"
        )