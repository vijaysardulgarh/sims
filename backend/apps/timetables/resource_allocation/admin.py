from django.contrib import admin

from .models import (
    ResourceAllocation,
)


@admin.register(
    ResourceAllocation
)
class ResourceAllocationAdmin(
    admin.ModelAdmin
):

    list_display = (
        "resource",
        "timetable_entry",
        "allocated_from",
        "allocated_to",
        "is_active",
    )

    search_fields = (
        "resource__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "is_active",
    )