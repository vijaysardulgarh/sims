from rest_framework import serializers

from apps.academics.streams.models import (
    Stream
)


class StreamSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Stream

        fields = [
            "id",
            "school",
            "name",
        ]

        read_only_fields = [
            "school"
        ]