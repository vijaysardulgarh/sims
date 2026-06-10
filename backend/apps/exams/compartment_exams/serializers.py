from rest_framework import serializers

from .models import (
    CompartmentExam
)


class CompartmentExamSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(
        source="student.full_name",
        read_only=True,
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True,
    )

    original_exam_name = serializers.CharField(
        source="original_exam.name",
        read_only=True,
    )

    class Meta:

        model = CompartmentExam

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