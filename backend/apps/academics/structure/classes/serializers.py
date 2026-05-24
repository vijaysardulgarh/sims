from rest_framework import serializers

from apps.academics.structure.classes.models import (
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