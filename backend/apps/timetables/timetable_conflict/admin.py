from django.contrib import admin

from .models import (
    TimetableConflict,
)


@admin.register(
    TimetableConflict
)
class TimetableConflictAdmin(
    admin.ModelAdmin
):

    list_display = (
        "conflict_type",
        "title",
        "timetable",
        "is_resolved",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "school",
        "academic_session",
        "conflict_type",
        "is_resolved",
    )

    readonly_fields = (
        "timetable",
        "timetable_entry",
        "conflict_type",
        "title",
        "description",
        "created_at",
    )

    def has_add_permission(
        self,
        request,
    ):
        return False

    def has_delete_permission(
        self,
        request,
        obj=None,
    ):
        return False