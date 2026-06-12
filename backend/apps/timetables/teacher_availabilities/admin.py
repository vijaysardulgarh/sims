from django.contrib import admin

from .models import (
    TeacherAvailability,
)


@admin.register(
    TeacherAvailability
)
class TeacherAvailabilityAdmin(
    admin.ModelAdmin
):

    list_display = (
        "teacher",
        "day",
        "period",
        "is_available",
        "is_active",
    )

    search_fields = (
        "teacher__first_name",
        "teacher__last_name",
    )

    list_filter = (
        "school",
        "academic_session",
        "day",
        "is_available",
        "is_active",
    )