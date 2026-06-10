from django.contrib import admin

from .models import (
    Timetable,
)


@admin.register(
    Timetable
)
class TimetableAdmin(
    admin.ModelAdmin
):

    list_display = (
        "name",
        "code",
        "school_class",
        "section",
        "bell_schedule",
        "effective_from",
        "effective_to",
        "is_published",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "school",
        "academic_session",
        "is_published",
        "is_active",
    )