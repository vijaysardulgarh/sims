from django.contrib import admin

from apps.users.models.role_model import (
    Role
)


# ==========================================
# ROLE ADMIN
# ==========================================

@admin.register(Role)
class RoleAdmin(
    admin.ModelAdmin
):

    list_display = (

        "id",

        "name",

        "code",

        "is_active",
    )

    search_fields = (

        "name",

        "code",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )