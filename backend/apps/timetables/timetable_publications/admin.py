from django.contrib import admin

from .models import (
    TimetablePublication,
)


@admin.register(
    TimetablePublication
)
class TimetablePublicationAdmin(
    admin.ModelAdmin
):

    list_display = (
        "timetable",
        "status",
        "published_by",
        "published_at",
        "is_active",
    )

    search_fields = (
        "status",
    )

    list_filter = (
        "school",
        "academic_session",
        "status",
        "is_active",
    )