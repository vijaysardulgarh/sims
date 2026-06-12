from rest_framework import serializers

from .models import (
    GradeCalculation
)


class GradeCalculationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = GradeCalculation

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