from rest_framework import serializers

from .models import (
    SubjectConstraint,
)


class SubjectConstraintSerializer(
    serializers.ModelSerializer
):

    school_class = serializers.CharField(
        source="subject_requirement.school_class.name",
        read_only=True,
    )

    section = serializers.CharField(
        source="subject_requirement.section.name",
        read_only=True,
    )

    subject = serializers.CharField(
        source="subject_requirement.subject.name",
        read_only=True,
    )

    theory_periods_per_week = serializers.IntegerField(
        source="subject_requirement.theory_periods_per_week",
        read_only=True,
    )

    lab_periods_per_week = serializers.IntegerField(
        source="subject_requirement.lab_periods_per_week",
        read_only=True,
    )

    total_periods_per_week = serializers.IntegerField(
        source="subject_requirement.total_periods_per_week",
        read_only=True,
    )

    is_compulsory = serializers.BooleanField(
        source="subject_requirement.is_compulsory",
        read_only=True,
    )

    class Meta:

        model = SubjectConstraint

        fields = (
            "id",
            "subject_requirement",

            "school_class",
            "section",
            "subject",

            "theory_periods_per_week",
            "lab_periods_per_week",
            "total_periods_per_week",
            "is_compulsory",

            "priority",
            "max_periods_per_day",
            "allow_consecutive_periods",
            "required_consecutive_periods",
            "spread_across_week",
            "avoid_first_period",
            "avoid_last_period",
            "preferred_time_slot",
            "remarks",

            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
        )

        read_only_fields = (
            "school_class",
            "section",
            "subject",
            "theory_periods_per_week",
            "lab_periods_per_week",
            "total_periods_per_week",
            "is_compulsory",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
        )