from rest_framework import serializers

from .models import (
    ResultApproval
)


class ResultApprovalSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(

        source=(
            "result.student.full_name"
        ),

        read_only=True,
    )

    exam_name = serializers.CharField(

        source=(
            "result.exam.name"
        ),

        read_only=True,
    )

    class Meta:

        model = ResultApproval

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