from django.contrib import admin

from .models import (
    SubjectConstraint,
)


@admin.register(
    SubjectConstraint
)
class SubjectConstraintAdmin(
    admin.ModelAdmin
):

    list_display = (
        "subject",
        "periods_per_week",
        "max_periods_per_day",
        "allow_consecutive_periods",
        "requires_room",
        "requires_resource",
        "is_active",
    )

    search_fields = (
        "subject__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "allow_consecutive_periods",
        "requires_room",
        "requires_resource",
        "is_active",
    )