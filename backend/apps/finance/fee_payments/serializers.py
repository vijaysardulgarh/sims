from rest_framework import serializers

from apps.finance.fee_payments.models import (
    FeePayment
)


class FeePaymentSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.CharField(
        source="student_fee.student.__str__",
        read_only=True
    )

    fee_structure_name = serializers.CharField(
        source="student_fee.fee_structure.name",
        read_only=True
    )

    created_by_name = serializers.CharField(
        source="created_by.username",
        read_only=True
    )

    class Meta:

        model = FeePayment

        fields = [

            "id",

            "school",

            "student_fee",

            "student_name",

            "fee_structure_name",

            "amount",

            "payment_mode",

            "payment_status",

            "transaction_id",

            "receipt_number",

            "payment_date",

            "remarks",

            "created_by",

            "created_by_name",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "receipt_number",

            "created_at",

            "updated_at",
        ]