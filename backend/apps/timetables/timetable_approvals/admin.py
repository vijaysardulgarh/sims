from django.contrib import admin

from .models import (
    TimetableApproval,
)


@admin.register(
    TimetableApproval
)
class TimetableApprovalAdmin(
    admin.ModelAdmin
):

    list_display = (
        "timetable",
        "status",
        "approved_by",
        "approved_at",
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