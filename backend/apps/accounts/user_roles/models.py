from django.db import models

from apps.core.common.base.models import (
    SchoolBaseModel
)

from apps.accounts.users.models import (
    User
)

from apps.accounts.roles.models import (
    Role
)


# ==========================================
# USER ROLE MODEL
# ==========================================

class UserRole(
    SchoolBaseModel
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

            "school",

            "user",

            "role",
        )

        ordering = [
            "id"
        ]

    def __str__(self):

        return (
            f"{self.user.email} - "
            f"{self.role.name}"
        )