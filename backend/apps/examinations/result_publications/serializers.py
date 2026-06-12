from rest_framework import serializers

from .models import (
    ResultPublication
)


class ResultPublicationSerializer(
    serializers.ModelSerializer
):

    exam_name = serializers.CharField(
        source="exam.name",
        read_only=True,
    )

    class Meta:

        model = ResultPublication

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