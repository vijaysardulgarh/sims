from django.contrib import admin

from .models import (
    TimetableEntry,
)


@admin.register(
    TimetableEntry
)
class TimetableEntryAdmin(
    admin.ModelAdmin
):

    list_display = (
        "timetable",
        "day",
        "period",
        "subject",
        "teacher",
        "is_active",
    )

    search_fields = (
        "subject__name",
        "teacher__first_name",
        "teacher__last_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "day",
        "subject",
        "is_active",
    )