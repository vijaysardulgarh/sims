from rest_framework import serializers
from .models import SubjectRequirement

class SubjectRequirementSerializer(serializers.ModelSerializer):
    school_class_name = serializers.CharField(
        source="school_class.name",
        read_only=True,
    )
    stream_name = serializers.CharField(
        source="stream.name",
        read_only=True,
        default="",
    )
    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True,
    )
    total_periods_per_week = serializers.ReadOnlyField()
    requires_lab = serializers.ReadOnlyField()

    class Meta:
        model = SubjectRequirement
        fields = (
            "id",
            "school_class",
            "school_class_name",
            "section",
            "stream",
            "stream_name",
            "sub_stream",
            "subject",
            "subject_name",
            "theory_periods_per_week",
            "lab_periods_per_week",
            "total_periods_per_week",
            "is_compulsory",
            "is_shared",
            "priority",
            "teachers_required",
            "requires_lab",
            "remarks",
            "is_active",
        )
        read_only_fields = (
            "school_class_name",
            "stream_name",
            "subject_name",
            "total_periods_per_week",
            "requires_lab",
        )