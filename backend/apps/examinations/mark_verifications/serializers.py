from rest_framework import serializers

from .models import (
    MarkVerification
)


class MarkVerificationSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(

        source=(
            "mark_entry.student.full_name"
        ),

        read_only=True,
    )

    subject_name = serializers.CharField(

        source=(
            "mark_entry.subject.name"
        ),

        read_only=True,
    )

    exam_name = serializers.CharField(

        source=(
            "mark_entry.exam.name"
        ),

        read_only=True,
    )

    class Meta:

        model = MarkVerification

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