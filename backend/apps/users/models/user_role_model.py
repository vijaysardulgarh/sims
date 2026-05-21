from django.db import models

from apps.core.models import (
    AuditBaseModel
)

from apps.users.models.user_model import (
    User
)

from apps.users.models.role_model import (
    Role
)


# ==========================================
# USER ROLE MODEL
# ==========================================

class UserRole(
    AuditBaseModel
):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )

    class Meta:

        unique_together = (
            "user",
            "role",
        )

    def __str__(self):

        return (
            f"{self.user.email} - "
            f"{self.role.name}"
        )