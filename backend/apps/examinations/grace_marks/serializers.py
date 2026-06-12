from rest_framework import serializers

from .models import (
    GraceMark
)


class GraceMarkSerializer(
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

    exam_name = serializers.CharField(
        source="exam.name",
        read_only=True,
    )

    class Meta:

        model = GraceMark

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

            "approved_at",
        ]

    def validate(self, attrs):

        original = attrs.get(
            "original_marks"
        )

        grace = attrs.get(
            "grace_marks"
        )

        final = attrs.get(
            "final_marks"
        )

        if final != (
            original + grace
        ):

            raise serializers.ValidationError(
                {
                    "final_marks":
                    (
                        "Final marks must "
                        "equal original "
                        "+ grace marks."
                    )
                }
            )

        return attrs