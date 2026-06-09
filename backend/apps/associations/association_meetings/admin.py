from django.contrib import admin

from apps.associations.models import (
    AssociationMeeting
)


@admin.register(AssociationMeeting)
class AssociationMeetingAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "school",
        "association",
        "academic_session",
        "meeting_date",
        "location",
    )

    search_fields = (
        "association__name",
        "location",
    )

    list_filter = (
        "school",
        "academic_session",
        "association",
    )

    date_hierarchy = (
        "meeting_date"
    )

    ordering = (
        "-meeting_date",
    )

    list_per_page = 25

    autocomplete_fields = (
        "association",
        "academic_session",
        "minutes_document",
    )

    list_select_related = (
        "school",
        "association",
        "academic_session",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )