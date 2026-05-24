from django.contrib import admin

from apps.academics.timetable.days.models import (
    Day
)


@admin.register(Day)
class DayAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "name",
        "school",
        "sequence",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "sequence",
    )

    list_per_page = 25