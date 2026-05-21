from django.contrib import admin

from apps.users.models.role_permission_model import (
    RolePermission
)


# ==========================================
# ROLE PERMISSION ADMIN
# ==========================================

@admin.register(RolePermission)
class RolePermissionAdmin(
    admin.ModelAdmin
):

    list_display = (

        "id",

        "role",

        "permission",

        "is_active",
    )

    list_filter = (

        "role",

        "permission",

        "is_active",
    )

    search_fields = (

        "role__name",

        "permission__name",
    )

    ordering = (
        "role",
    )