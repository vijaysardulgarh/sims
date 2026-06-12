from django.contrib import admin

from .models import (
    SubstituteAssignment,
)


@admin.register(
    SubstituteAssignment
)
class SubstituteAssignmentAdmin(
    admin.ModelAdmin
):

    list_display = (
        "substitution_date",
        "original_teacher",
        "substitute_teacher",
        "timetable_entry",
        "is_active",
    )

    search_fields = (
        "original_teacher__first_name",
        "substitute_teacher__first_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "substitution_date",
        "is_active",
    )