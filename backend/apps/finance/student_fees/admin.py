from django.contrib import admin

from apps.finance.student_fees.models import (
    StudentFee
)


@admin.register(StudentFee)
class StudentFeeAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "student",
        "session",
        "total_amount",
        "paid_amount",
        "due_amount",
        "is_closed",
        "school",
    )

    search_fields = (

        "student__first_name",

        "student__last_name",

        "session",
    )

    list_filter = (
        "school",
        "session",
        "is_closed",
    )

    ordering = (
        "-created_at",
    )

    autocomplete_fields = (
        "student",
        "fee_structure",
    )

    list_select_related = (
        "school",
        "student",
        "fee_structure",
    )

    readonly_fields = (
        "total_amount",
        "due_amount",
        "payment_count",
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    fieldsets = (

        (
            "Student Fee Information",
            {
                "fields": (

                    "school",

                    "student",

                    "fee_structure",

                    "session",
                )
            }
        ),

        (
            "Fee Details",
            {
                "fields": (

                    "total_amount",

                    "paid_amount",

                    "due_amount",

                    "payment_count",

                    "is_closed",
                )
            }
        ),

        (
            "Additional Information",
            {
                "fields": (
                    "remarks",
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