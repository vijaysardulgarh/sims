from django.contrib import admin

from apps.users.models.user_role_model import (
    UserRole
)


# ==========================================
# USER ROLE ADMIN
# ==========================================

@admin.register(UserRole)
class UserRoleAdmin(
    admin.ModelAdmin
):

    list_display = (

        "id",

        "user",

        "role",

        "is_active",
    )

    list_filter = (

        "role",

        "is_active",
    )

    search_fields = (

        "user__email",

        "role__name",
    )

    ordering = (
        "user",
    )