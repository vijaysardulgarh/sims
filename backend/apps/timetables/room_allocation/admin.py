from django.contrib import admin

from .models import (
    RoomAllocation,
)


@admin.register(
    RoomAllocation
)
class RoomAllocationAdmin(
    admin.ModelAdmin
):

    list_display = (
        "room",
        "timetable_entry",
        "is_active",
    )

    search_fields = (
        "room__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "is_active",
    )