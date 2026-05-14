from rest_framework import serializers

from apps.academics.sections import (
    Section
)


class SectionSerializer(
    serializers.ModelSerializer
):

    class_name = serializers.CharField(
        source="class_obj.name",
        read_only=True
    )

    stream_name = serializers.CharField(
        source="stream.name",
        read_only=True
    )

    medium_name = serializers.CharField(
        source="medium.name",
        read_only=True
    )

    classroom_name = serializers.CharField(
        source="classroom.name",
        read_only=True
    )

    class Meta:

        model = Section

        fields = "__all__"

        read_only_fields = [
            "school"
        ]