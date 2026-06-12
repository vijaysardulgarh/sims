from rest_framework import serializers

from .models import (
    BestOfSubject
)


class BestOfSubjectSerializer(
    serializers.ModelSerializer
):

    exam_name = serializers.CharField(
        source="exam.name",
        read_only=True,
    )

    class Meta:

        model = BestOfSubject

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