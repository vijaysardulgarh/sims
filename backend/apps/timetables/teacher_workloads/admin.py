from django.contrib import admin

from .models import (
    TeacherWorkload,
)


@admin.register(
    TeacherWorkload
)
class TeacherWorkloadAdmin(
    admin.ModelAdmin
):

    list_display = (
        "teacher",
        "max_periods_per_day",
        "max_periods_per_week",
        "max_consecutive_periods",
        "allow_overtime",
        "is_active",
    )

    search_fields = (
        "teacher__first_name",
        "teacher__last_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "allow_overtime",
        "is_active",
    )