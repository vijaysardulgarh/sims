from django.contrib import admin

from apps.academics.curriculum.subjects.models import (
    Subject
)


@admin.register(Subject)
class SubjectAdmin(
    admin.ModelAdmin
):

    # ============================================
    # LIST DISPLAY
    # ============================================

    list_display = (

        "id",

        "name",

        "code",

        "school",

        "is_language",

        "is_optional",

        "has_lab",

        "is_active",
    )

    # ============================================
    # SEARCH
    # ============================================

    search_fields = (

        "name",

        "code",

        "school__name",
    )

    # ============================================
    # FILTERS
    # ============================================

    list_filter = (

        "school",

        "is_language",

        "is_optional",

        "has_lab",

        "is_active",
    )

    # ============================================
    # ORDERING
    # ============================================

    ordering = (
        "name",
    )

    # ============================================
    # PAGINATION
    # ============================================

    list_per_page = 25

    # ============================================
    # READONLY
    # ============================================

    readonly_fields = (

        "created_at",

        "updated_at",
    )

    # ============================================
    # FIELDSETS
    # ============================================

    fieldsets = (

        ("Basic Information", {

            "fields": (

                "school",

                "name",

                "code",
            )
        }),

        ("Subject Configuration", {

            "fields": (

                "is_language",

                "is_optional",

                "has_lab",
            )
        }),

        ("Status", {

            "fields": (

                "is_active",

                "is_deleted",
            )
        }),

        ("System Information", {

            "fields": (

                "created_at",

                "updated_at",
            )
        }),
    )