from rest_framework import serializers

from apps.library.book_accessions.models import (
    BookAccession
)


class BookAccessionSerializer(
    serializers.ModelSerializer
):

    book_title = serializers.CharField(
        source="book.title",
        read_only=True
    )

    class Meta:

        model = BookAccession

        fields = [

            "id",

            "school",

            "book",

            "book_title",

            "accession_number",

            "barcode",

            "purchase_date",

            "price",

            "vendor",

            "source",

            "rack_number",

            "shelf_number",

            "condition",

            "status",

            "remarks",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "school",

            "created_at",

            "updated_at",
        ]