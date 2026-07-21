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
        "school_class",
        "section",
        "subject",
        "priority",
        "max_periods_per_day",
        "allow_consecutive_periods",
        "required_consecutive_periods",
        "spread_across_week",
        "avoid_first_period",
        "avoid_last_period",
        "preferred_time_slot",
        "is_active",
    )

    search_fields = (
        "subject_requirement__school_class__name",
        "subject_requirement__section__name",
        "subject_requirement__subject__name",
    )

    list_filter = (
        "school",
        "academic_session",
        "preferred_time_slot",
        "allow_consecutive_periods",
        "spread_across_week",
        "avoid_first_period",
        "avoid_last_period",
        "is_active",
    )

    ordering = (
        "subject_requirement__school_class__display_order",
        "subject_requirement__subject__name",
    )

    autocomplete_fields = (
        "subject_requirement",
    )

    @admin.display(
        description="Class",
        ordering="subject_requirement__school_class__name",
    )
    def school_class(
        self,
        obj,
    ):

        return (
            obj.subject_requirement.school_class.name
        )

    @admin.display(
        description="Section",
        ordering="subject_requirement__section__name",
    )
    def section(
        self,
        obj,
    ):

        if obj.subject_requirement.section:

            return (
                obj.subject_requirement.section.name
            )

        return "-"

    @admin.display(
        description="Subject",
        ordering="subject_requirement__subject__name",
    )
    def subject(
        self,
        obj,
    ):

        return (
            obj.subject_requirement.subject.name
        )