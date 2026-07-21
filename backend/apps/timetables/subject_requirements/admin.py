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
        "stream",
        "sub_stream",
        "subject",
        "theory_periods_per_week",
        "lab_periods_per_week",
        "total_periods_per_week",
        "requires_lab",
        "is_compulsory",
        "is_shared",
        "is_active",
    )

    search_fields = (
        "school_class__name",
        "section__name",
        "stream__name",
        "sub_stream",
        "subject__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "school_class",
        "section",
        "stream",
        "is_compulsory",
        "is_shared",
        "is_active",
    )

    ordering = (
        "school_class__display_order",
        "subject__name",
    )

    autocomplete_fields = (
        "school_class",
        "section",
        "stream",
        "subject",
    )

    @admin.display(
        description="Total Periods/Week",
    )
    def total_periods_per_week(
        self,
        obj,
    ):

        return obj.total_periods_per_week

    @admin.display(
        boolean=True,
        description="Lab",
    )
    def requires_lab(
        self,
        obj,
    ):

        return obj.requires_lab