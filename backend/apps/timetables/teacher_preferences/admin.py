from django.contrib import admin

from .models import TeacherPreference


@admin.register(TeacherPreference)
class TeacherPreferenceAdmin(admin.ModelAdmin):

    list_display = (
        "teacher",
        "preferred_shift",
        "maximum_free_gaps",
        "prefer_first_period",
        "avoid_first_period",
        "prefer_last_period",
        "avoid_last_period",
        "is_active",
    )

    search_fields = (
        "teacher__name",
        "teacher__employee_id",
    )

    list_filter = (
        "school",
        "academic_session",
        "preferred_shift",
        "prefer_first_period",
        "avoid_first_period",
        "prefer_last_period",
        "avoid_last_period",
        "is_active",
    )

    ordering = (
        "teacher__name",
    )

    autocomplete_fields = (
        "teacher",
    )