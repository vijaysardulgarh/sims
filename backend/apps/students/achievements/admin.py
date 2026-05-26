from django.contrib import admin

from apps.students.achievements.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    # =====================================
    # LIST DISPLAY
    # =====================================

    list_display = (

        "id",

        "student_name",

        "achievement_type",

        "event_name",

        "rank",

        "reward_title",

        "school",

        "is_active",

        "date",

        "created_at",
    )

    # =====================================
    # SEARCH
    # =====================================

    search_fields = (

        "student_name",

        "event_name",

        "reward_title",

        "remarks",
    )

    # =====================================
    # FILTERS
    # =====================================

    list_filter = (

        "achievement_type",

        "school",

        "is_active",

        "is_deleted",

        "date",

        "created_at",
    )

    # =====================================
    # ORDERING
    # =====================================

    ordering = (

        "-date",

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

        "created_at",

        "updated_at",
    )

    # =====================================
    # FIELDSETS
    # =====================================

    fieldsets = (

        (
            "Achievement Information",
            {
                "fields": (

                    "school",

                    "student_name",

                    "achievement_type",

                    "event_name",

                    "rank",

                    "reward_title",

                    "date",

                    "remarks",
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