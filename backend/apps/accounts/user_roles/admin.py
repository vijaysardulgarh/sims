from django.contrib import admin

from apps.accounts.user_roles.models import (
    UserRole
)


# ==========================================
# USER ROLE ADMIN
# ==========================================

@admin.register(UserRole)
class UserRoleAdmin(
    admin.ModelAdmin
):

    # ======================================
    # LIST DISPLAY
    # ======================================

    list_display = (

        "id",

        "user",

        "role",

        "school",

        "is_active",

        "created_at",
    )

    # ======================================
    # FILTERS
    # ======================================

    list_filter = (

        "school",

        "role",

        "is_active",

        "created_at",
    )

    # ======================================
    # SEARCH
    # ======================================

    search_fields = (

        "user__email",

        "user__username",

        "role__name",

        "school__name",
    )

    # ======================================
    # ORDERING
    # ======================================

    ordering = (
        "user",
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
            "User Role Information",

            {
                "fields": (

                    "school",

                    "user",

                    "role",

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