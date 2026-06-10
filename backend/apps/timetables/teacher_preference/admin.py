from django.contrib import admin

from .models import (
    TeacherPreference,
)


@admin.register(
    TeacherPreference
)
class TeacherPreferenceAdmin(
    admin.ModelAdmin
):

    list_display = (
        "teacher",
        "max_periods_per_day",
        "max_periods_per_week",
        "prefer_consecutive_periods",
        "avoid_gaps_between_classes",
        "is_active",
    )

    search_fields = (
        "teacher__first_name",
        "teacher__last_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "prefer_first_period",
        "avoid_first_period",
        "prefer_last_period",
        "avoid_last_period",
        "is_active",
    )