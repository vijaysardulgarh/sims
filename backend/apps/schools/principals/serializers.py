from rest_framework import serializers

from .models import Principal


class PrincipalSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True,
    )

    class Meta:

        model = Principal

        fields = [
            "id",
            "school",
            "school_name",
            "name",
            "photo",
            "qualification",
            "message",
            "joining_date",
            "display_order",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]

        read_only_fields = [
            "id",
            "school_name",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]