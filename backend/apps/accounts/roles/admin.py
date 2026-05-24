from django.contrib import admin

from apps.accounts.roles.models import (
    Role
)


# ==========================================
# ROLE ADMIN
# ==========================================

@admin.register(Role)
class RoleAdmin(
    admin.ModelAdmin
):

    # ======================================
    # LIST DISPLAY
    # ======================================

    list_display = (

        "id",

        "name",

        "code",

        "school",

        "is_active",

        "is_system_role",

        "created_at",
    )

    # ======================================
    # SEARCH
    # ======================================

    search_fields = (

        "name",

        "code",

        "school__name",
    )

    # ======================================
    # FILTERS
    # ======================================

    list_filter = (

        "school",

        "is_active",

        "is_system_role",

        "created_at",
    )

    # ======================================
    # ORDERING
    # ======================================

    ordering = (
        "name",
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
            "Basic Information",

            {
                "fields": (

                    "school",

                    "name",

                    "code",

                    "description",
                )
            }
        ),

        (
            "Status",

            {
                "fields": (

                    "is_active",

                    "is_system_role",
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

    # ======================================
    # DELETE PROTECTION
    # ======================================

    def has_delete_permission(
        self,
        request,
        obj=None
    ):

        if obj and obj.is_system_role:

            return False

        return super().has_delete_permission(
            request,
            obj
        )