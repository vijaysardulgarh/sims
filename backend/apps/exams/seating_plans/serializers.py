from rest_framework import serializers

from .models import (
    SeatingPlan
)


class SeatingPlanSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(
        source="student.full_name",
        read_only=True,
    )

    exam_name = serializers.CharField(
        source="exam.name",
        read_only=True,
    )

    class Meta:

        model = SeatingPlan

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