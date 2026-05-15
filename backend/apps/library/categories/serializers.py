from rest_framework import serializers

from apps.library.categories.models import (
    BookCategory
)


class BookCategorySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = BookCategory

        fields = [

            "id",

            "school",

            "name",

            "code",

            "description",

            "is_active",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "school",

            "created_at",

            "updated_at",
        ]