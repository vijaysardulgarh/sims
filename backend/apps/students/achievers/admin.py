from django.contrib import admin

from apps.students.achievers.models import Achiever


@admin.register(Achiever)
class AchieverAdmin(admin.ModelAdmin):

    # =====================================
    # LIST DISPLAY
    # =====================================

    list_display = (

        "id",

        "achievement",

        "school",

        "obtained_marks",

        "total_marks",

        "percentage",

        "is_active",

        "created_at",
    )

    # =====================================
    # SEARCH
    # =====================================

    search_fields = (

        "achievement__student_name",

        "achievement__event_name",
    )

    # =====================================
    # FILTERS
    # =====================================

    list_filter = (

        "school",

        "is_active",

        "is_deleted",

        "created_at",
    )

    # =====================================
    # ORDERING
    # =====================================

    ordering = (

        "-created_at",
    )

    # =====================================
    # PAGINATION
    # =====================================

    list_per_page = 25

    # =====================================
    # READONLY FIELDS
    # =====================================

    readonly_fields = (

        "percentage",

        "created_at",

        "updated_at",
    )

    # =====================================
    # FIELDSETS
    # =====================================

    fieldsets = (

        (
            "Achiever Information",
            {
                "fields": (

                    "school",

                    "achievement",

                    "obtained_marks",

                    "total_marks",

                    "percentage",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (

                    "is_active",

                    "is_deleted",
                )
            },
        ),

        (
            "Audit Information",
            {
                "fields": (

                    "created_by",

                    "updated_by",

                    "created_at",

                    "updated_at",
                )
            },
        ),
    )