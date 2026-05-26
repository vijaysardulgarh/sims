from django.contrib import admin

from apps.accounts.permissions.models import (
    Permission
)


# ==========================================
# PERMISSION ADMIN
# ==========================================

@admin.register(Permission)
class PermissionAdmin(
    admin.ModelAdmin
):

    # ======================================
    # LIST DISPLAY
    # ======================================

    list_display = (

        "id",

        "name",

        "code",

        "module",

        "action",

        "display_order",

        "is_active",

        "is_system_permission",

        "created_at",
    )

    # ======================================
    # SEARCH
    # ======================================

    search_fields = (

        "name",

        "code",

        "module__name",
    )

    # ======================================
    # FILTERS
    # ======================================

    list_filter = (

        "module",

        "action",

        "is_active",

        "is_system_permission",

        "created_at",
    )

    # ======================================
    # ORDERING
    # ======================================

    ordering = (

        "module",

        "display_order",

        "name",
    )

    # ======================================
    # READONLY FIELDS
    # ======================================

    readonly_fields = (

        "name",

        "code",

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
            "Permission Information",

            {
                "fields": (

                    "module",

                    "action",

                    "name",

                    "code",

                    "description",
                )
            }
        ),

        (
            "System Settings",

            {
                "fields": (

                    "is_active",

                    "is_system_permission",

                    "display_order",
                )
            }
        ),

        (
            "Audit Information",

            {
                "classes": ("collapse",),

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
    # AUTO SELECT RELATED
    # ======================================

    list_select_related = (
        "module",
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

        if obj and obj.is_system_permission:

            return False

        return super().has_delete_permission(
            request,
            obj
        )