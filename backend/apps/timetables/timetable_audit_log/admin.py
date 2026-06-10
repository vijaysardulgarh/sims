from django.contrib import admin

from .models import (
    TimetableAuditLog,
)


@admin.register(
    TimetableAuditLog
)
class TimetableAuditLogAdmin(
    admin.ModelAdmin
):

    list_display = (
        "timetable",
        "action",
        "field_name",
        "created_by",
        "created_at",
    )

    search_fields = (
        "action",
        "field_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "action",
        "created_at",
    )

    readonly_fields = (
        "timetable",
        "timetable_entry",
        "action",
        "field_name",
        "old_value",
        "new_value",
        "remarks",
        "created_by",
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