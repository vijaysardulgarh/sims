from django.contrib import admin

from apps.schools.branches.models import (
    Branch
)


# ==========================================
# BRANCH ADMIN
# ==========================================

@admin.register(Branch)
class BranchAdmin(
    admin.ModelAdmin
):

    # ======================================
    # TABLE DISPLAY
    # ======================================

    list_display = (

        "id",

        "name",

        "code",

        "school",

        "phone",

        "is_active",

        "created_at",
    )

    list_display_links = (

        "id",

        "name",
    )

    # ======================================
    # SEARCH
    # ======================================

    search_fields = (

        "name",

        "code",

        "school__name",

        "phone",
    )

    # ======================================
    # FILTERS
    # ======================================

    list_filter = (

        "school",

        "is_active",

        "is_deleted",
    )

    # ======================================
    # ORDERING
    # ======================================

    ordering = (
        "name",
    )

    # ======================================
    # PAGINATION
    # ======================================

    list_per_page = 25

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
            "Branch Information",

            {
                "fields": (

                    "school",

                    "name",

                    "code",
                )
            }
        ),

        (
            "Contact Information",

            {
                "fields": (

                    "phone",

                    "address",
                )
            }
        ),

        (
            "Status",

            {
                "fields": (

                    "is_active",

                    "is_deleted",
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