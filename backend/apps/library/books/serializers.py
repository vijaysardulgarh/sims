from rest_framework import serializers

from apps.library.books.models import (
    Book
)


class BookSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Book

        fields = [

            "id",

            "school",

            "title",

            "isbn",

            "author",

            "publisher",

            "category",

            "language",

            "total_copies",

            "available_copies",

            "rack_number",

            "price",

            "status",

            "description",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "school",

            "created_at",

            "updated_at",
        ]