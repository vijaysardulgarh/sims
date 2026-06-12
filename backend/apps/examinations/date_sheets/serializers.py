from rest_framework import serializers

from .models import (
    DateSheet
)


class DateSheetSerializer(
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

    class_name = serializers.CharField(
        source="class_obj.name",
        read_only=True,
    )

    section_name = serializers.CharField(
        source="section.name",
        read_only=True,
    )

    class Meta:

        model = DateSheet

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