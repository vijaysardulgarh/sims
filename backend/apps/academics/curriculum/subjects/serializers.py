from rest_framework import serializers

from apps.academics.curriculum.subjects.models import (
    Subject
)


class SubjectSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Subject

        fields = [
            "id",
            "school",
            "name",
            "code",
        ]

        read_only_fields = [
            "school"
        ]