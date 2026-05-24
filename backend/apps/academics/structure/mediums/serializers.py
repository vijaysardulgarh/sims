from rest_framework import serializers

from apps.academics.structure.mediums.models import (
    Medium
)


class MediumSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Medium

        fields = [
            "id",
            "school",
            "name",
        ]

        read_only_fields = [
            "school"
        ]