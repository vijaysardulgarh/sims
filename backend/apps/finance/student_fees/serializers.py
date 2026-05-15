from rest_framework import serializers

from apps.finance.student_fees.models import (
    StudentFee
)


class StudentFeeSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(
        source="student.__str__",
        read_only=True
    )

    class_name = serializers.CharField(
        source="fee_structure.class_obj.name",
        read_only=True
    )

    stream_name = serializers.CharField(
        source="fee_structure.stream.name",
        read_only=True
    )

    payment_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:

        model = StudentFee

        fields = [

            "id",

            "school",

            "student",

            "student_name",

            "fee_structure",

            "class_name",

            "stream_name",

            "total_amount",

            "paid_amount",

            "due_amount",

            "session",

            "is_closed",

            "payment_count",

            "remarks",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "school",

            "total_amount",

            "due_amount",

            "payment_count",

            "created_at",

            "updated_at",
        ]