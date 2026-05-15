from django.contrib import admin

from apps.library.book_accessions.models import (
    BookAccession
)


@admin.register(BookAccession)
class BookAccessionAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "accession_number",
        "book",
        "barcode",
        "status",
        "condition",
        "rack_number",
        "shelf_number",
        "school",
    )

    search_fields = (

        "accession_number",

        "barcode",

        "book__title",

        "vendor",
    )

    list_filter = (
        "school",
        "status",
        "condition",
    )

    ordering = (
        "-created_at",
    )

    autocomplete_fields = (
        "book",
    )

    list_select_related = (
        "school",
        "book",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    fieldsets = (

        (
            "Book Information",
            {
                "fields": (

                    "school",

                    "book",

                    "accession_number",

                    "barcode",
                )
            }
        ),

        (
            "Purchase Information",
            {
                "fields": (

                    "purchase_date",

                    "price",

                    "vendor",

                    "source",
                )
            }
        ),

        (
            "Library Location",
            {
                "fields": (

                    "rack_number",

                    "shelf_number",
                )
            }
        ),

        (
            "Book Status",
            {
                "fields": (

                    "condition",

                    "status",

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