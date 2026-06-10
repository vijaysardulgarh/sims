from django.contrib import admin

from .models import (
    SubjectRequirement,
)


@admin.register(
    SubjectRequirement
)
class SubjectRequirementAdmin(
    admin.ModelAdmin
):

    list_display = (
        "school_class",
        "section",
        "subject",
        "periods_per_week",
        "periods_per_day",
        "is_mandatory",
        "is_active",
    )

    search_fields = (
        "subject__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "school_class",
        "is_mandatory",
        "is_active",
    )