from django.contrib import admin

from apps.finance.fee_payments.models import (
    FeePayment
)


@admin.register(FeePayment)
class FeePaymentAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "receipt_number",
        "student_fee",
        "amount",
        "payment_mode",
        "payment_status",
        "payment_date",
        "school",
    )

    search_fields = (

        "receipt_number",

        "student_fee__student__first_name",

        "student_fee__student__last_name",

        "transaction_id",
    )

    list_filter = (
        "school",
        "payment_mode",
        "payment_status",
        "payment_date",
    )

    ordering = (
        "-created_at",
    )

    autocomplete_fields = (
        "student_fee",
        "created_by",
    )

    list_select_related = (
        "student_fee",
        "school",
        "created_by",
    )

    readonly_fields = (
        "receipt_number",
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    fieldsets = (

        (
            "Payment Information",
            {
                "fields": (

                    "school",

                    "student_fee",

                    "amount",

                    "payment_mode",

                    "payment_status",

                    "transaction_id",

                    "receipt_number",

                    "payment_date",
                )
            }
        ),

        (
            "Additional Information",
            {
                "fields": (
                    "remarks",
                    "created_by",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),
    )