from rest_framework import serializers

from apps.academics.mediums import (
    Medium
)


class MediumSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Medium

        fields = "__all__"

        read_only_fields = [
            "school"
        ]