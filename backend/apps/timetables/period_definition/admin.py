from django.contrib import admin

from .models import (
    PeriodDefinition,
)


@admin.register(
    PeriodDefinition
)
class PeriodDefinitionAdmin(
    admin.ModelAdmin
):

    list_display = (
        "name",
        "code",
        "bell_schedule",
        "start_time",
        "end_time",
        "display_order",
        "is_instructional",
        "is_break",
        "is_lunch",
        "is_assembly",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "school",
        "academic_session",
        "bell_schedule",
        "is_break",
        "is_lunch",
        "is_assembly",
        "is_active",
    )

    ordering = (
        "display_order",
        "start_time",
    )