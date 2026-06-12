from rest_framework import serializers

from .models import (
    ExamType
)


class ExamTypeSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ExamType

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