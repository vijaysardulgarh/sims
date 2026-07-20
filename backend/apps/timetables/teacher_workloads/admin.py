from django.contrib import admin

from .models import TeacherWorkload


@admin.register(TeacherWorkload)
class TeacherWorkloadAdmin(admin.ModelAdmin):

    list_display = (
        "teacher",
        "max_periods_per_day",
        "min_periods_per_day",
        "max_periods_per_week",
        "min_periods_per_week",
        "max_consecutive_periods",
        "school",
        "academic_session",
        "is_active",
    )

    search_fields = (
        "teacher__name",
        "teacher__employee_id",
    )

    list_filter = (
        "school",
        "academic_session",
        "is_active",
    )

    ordering = (
        "teacher__name",
    )

    autocomplete_fields = (
        "teacher",
    )