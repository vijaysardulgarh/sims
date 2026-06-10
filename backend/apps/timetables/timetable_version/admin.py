from django.contrib import admin

from .models import (
    TimetableVersion,
)


@admin.register(
    TimetableVersion
)
class TimetableVersionAdmin(
    admin.ModelAdmin
):

    list_display = (
        "timetable",
        "version_number",
        "version_name",
        "is_current",
        "created_at",
    )

    search_fields = (
        "version_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "is_current",
    )