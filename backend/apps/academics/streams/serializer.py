from rest_framework import serializers

from apps.academics.streams import (
    Stream
)


class StreamSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Stream

        fields = "__all__"

        read_only_fields = [
            "school"
        ]