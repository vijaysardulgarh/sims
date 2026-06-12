from rest_framework import serializers

from .models import (
    SubjectConfiguration
)


class SubjectConfigurationSerializer(
    serializers.ModelSerializer
):

    exam_name = serializers.CharField(
        source="exam.name",
        read_only=True,
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True,
    )

    class Meta:

        model = (
            SubjectConfiguration
        )

        fields = "__all__"

        read_only_fields = [

            "school",

            "academic_session",

            "created_by",

            "updated_by",

            "deleted_by",

            "created_at",

            "updated_at",

            "deleted_at",
        ]