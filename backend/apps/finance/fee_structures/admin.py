from django.contrib import admin

from apps.finance.fee_structures.models import (
    FeeStructure
)


@admin.register(FeeStructure)
class FeeStructureAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "class_obj",
        "stream",
        "session",
        "total_fee",
        "is_active",
        "school",
    )

    search_fields = (

        "class_obj__name",

        "stream__name",

        "session",
    )

    list_filter = (
        "school",
        "session",
        "is_active",
    )

    ordering = (
        "-created_at",
    )

    autocomplete_fields = (
        "class_obj",
        "stream",
    )

    list_select_related = (
        "school",
        "class_obj",
        "stream",
    )

    readonly_fields = (
        "total_fee",
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    fieldsets = (

        (
            "Academic Information",
            {
                "fields": (

                    "school",

                    "class_obj",

                    "stream",

                    "session",
                )
            }
        ),

        (
            "Fee Structure",
            {
                "fields": (

                    "admission_fee",

                    "rcf",

                    "cwf",

                    "ccwf",

                    "other_fee",

                    "total_fee",
                )
            }
        ),

        (
            "Status Information",
            {
                "fields": (
                    "is_active",
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