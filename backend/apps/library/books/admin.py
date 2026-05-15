from django.contrib import admin

from apps.library.books.models import (
    Book
)


@admin.register(Book)
class BookAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "title",
        "author",
        "isbn",
        "category",
        "total_copies",
        "available_copies",
        "status",
        "school",
    )

    search_fields = (

        "title",

        "author",

        "isbn",

        "publisher",
    )

    list_filter = (
        "school",
        "category",
        "status",
        "language",
    )

    ordering = (
        "title",
    )

    list_select_related = (
        "school",
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

                    "title",

                    "isbn",

                    "author",

                    "publisher",
                )
            }
        ),

        (
            "Classification",
            {
                "fields": (

                    "category",

                    "language",

                    "rack_number",
                )
            }
        ),

        (
            "Inventory",
            {
                "fields": (

                    "total_copies",

                    "available_copies",

                    "price",

                    "status",
                )
            }
        ),

        (
            "Additional Information",
            {
                "fields": (
                    "description",
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