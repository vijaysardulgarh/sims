from django.contrib import admin

from .models import (
    WorkingDay,
)


@admin.register(
    WorkingDay
)
class WorkingDayAdmin(
    admin.ModelAdmin
):

    list_display = (
        "day_code",
        "display_order",
        "is_working_day",
        "is_half_day",
        "is_active",
    )

    search_fields = (
        "day_code",
    )

    list_filter = (
        "school",
        "academic_session",
        "is_working_day",
        "is_half_day",
        "is_active",
    )

    ordering = (
        "display_order",
    )