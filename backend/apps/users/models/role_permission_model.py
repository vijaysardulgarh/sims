from django.db import models

from apps.core.models import (
    AuditBaseModel
)

from apps.users.models.role_model import (
    Role
)

from apps.users.models.access_control_model import (
    AccessControl
)


# ==========================================
# ROLE PERMISSION MODEL
# ==========================================

class RolePermission(
    AuditBaseModel
):

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="role_permissions"
    )

    permission = models.ForeignKey(
        AccessControl,
        on_delete=models.CASCADE,
        related_name="role_permissions"
    )

    class Meta:

        unique_together = (
            "role",
            "permission"
        )

    def __str__(self):

        return (
            f"{self.role.name} - "
            f"{self.permission.code}"
        )