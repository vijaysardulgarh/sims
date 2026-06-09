from rest_framework import serializers

from .models import (
    CommunicationCategory
)


class CommunicationCategorySerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = CommunicationCategory

        fields = "__all__"

        read_only_fields = [

            "school",

            "created_at",
            "updated_at",

            "created_by",
            "updated_by",
        ]