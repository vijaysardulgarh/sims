# exams - serializers.py
from rest_framework import serializers

from .models import (
    Exam
)


class ExamSerializer(
    serializers.ModelSerializer
):

    exam_type_name = serializers.CharField(

        source="exam_type.name",

        read_only=True,
    )

    class Meta:

        model = Exam

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