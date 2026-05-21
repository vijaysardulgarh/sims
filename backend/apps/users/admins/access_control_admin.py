from django.contrib import admin

from apps.users.models.access_control_model import (
    AccessControl
)


# ==========================================
# ACCESS CONTROL ADMIN
# ==========================================

@admin.register(AccessControl)
class AccessControlAdmin(
    admin.ModelAdmin
):

    list_display = (

        "id",

        "name",

        "code",

        "module",

        "is_active",
    )

    search_fields = (

        "name",

        "code",

        "module",
    )

    list_filter = (

        "module",

        "is_active",
    )

    ordering = (

        "module",

        "name",
    )