from rest_framework import serializers

from apps.finance.fee_structures.models import (
    FeeStructure
)


class FeeStructureSerializer(
    serializers.ModelSerializer
):

    class_name = serializers.CharField(
        source="class_obj.name",
        read_only=True
    )

    stream_name = serializers.CharField(
        source="stream.name",
        read_only=True
    )

    total_fee = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:

        model = FeeStructure

        fields = [

            "id",

            "school",

            "class_obj",

            "class_name",

            "stream",

            "stream_name",

            "session",

            "admission_fee",

            "rcf",

            "cwf",

            "ccwf",

            "other_fee",

            "total_fee",

            "is_active",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "school",

            "total_fee",

            "created_at",

            "updated_at",
        ]