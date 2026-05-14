from rest_framework import serializers

from apps.academics.classes import (
    Class
)


class ClassSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Class

        fields = "__all__"

        read_only_fields = [
            "school"
        ]