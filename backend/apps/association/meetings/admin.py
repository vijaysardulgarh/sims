# =============================================================================
# meetings/admin/meeting_admin.py
# =============================================================================

from django.contrib import admin

from apps.associations.meetings.models import Meeting


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "group",
        "academic_session",
        "meeting_date",
        "location",
    )

    search_fields = (
        "group__name",
        "location",
    )

    list_filter = (
        "academic_session",
        "group",
        "meeting_date",
    )

    ordering = (
        "-meeting_date",
    )

    list_per_page = 25

    autocomplete_fields = (
        "group",
        "academic_session",
        "minutes_document",
    )

    list_select_related = (
        "group",
        "academic_session",
    )