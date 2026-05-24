from django.contrib import admin

from apps.accounts.role_permissions.models import (
    RolePermission
)


# ==========================================
# ROLE PERMISSION ADMIN
# ==========================================

@admin.register(RolePermission)
class RolePermissionAdmin(
    admin.ModelAdmin
):

    # ======================================
    # LIST DISPLAY
    # ======================================

    list_display = (

        "id",

        "school",

        "role",

        "permission",

        "is_active",

        "created_at",
    )

    # ======================================
    # FILTERS
    # ======================================

    list_filter = (

        "school",

        "role",

        "permission__module",

        "is_active",

        "created_at",
    )

    # ======================================
    # SEARCH
    # ======================================

    search_fields = (

        "role__name",

        "permission__name",

        "permission__code",

        "school__name",
    )

    # ======================================
    # ORDERING
    # ======================================

    ordering = (

        "school",

        "role",
    )

    # ======================================
    # READONLY FIELDS
    # ======================================

    readonly_fields = (

        "created_at",

        "updated_at",

        "created_by",

        "updated_by",
    )

    # ======================================
    # FIELDSETS
    # ======================================

    fieldsets = (

        (
            "Role Permission Information",

            {
                "fields": (

                    "school",

                    "role",

                    "permission",

                    "is_active",
                )
            }
        ),

        (
            "Audit Information",

            {
                "fields": (

                    "created_at",

                    "updated_at",

                    "created_by",

                    "updated_by",
                )
            }
        ),
    )

    # ======================================
    # SAVE MODEL
    # ======================================

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        if not change:

            obj.created_by = (
                request.user
            )

        obj.updated_by = (
            request.user
        )

        super().save_model(

            request,

            obj,

            form,

            change
        )