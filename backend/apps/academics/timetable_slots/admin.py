from django.contrib import admin

from apps.academics.timetable_slots import (
    TimetableSlot
)


@admin.register(TimetableSlot)
class TimetableSlotAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "school",
        "day",
        "sequence_number",
        "period_number",
        "start_time",
        "end_time",
        "is_break",
        "is_assembly",
        "is_special_event",
    )

    search_fields = (
        "day__name",
        "school__name",
    )

    list_filter = (
        "school",
        "day",
        "is_break",
        "is_assembly",
        "is_special_event",
    )

    ordering = (
        "day",
        "sequence_number",
    )

    list_per_page = 25