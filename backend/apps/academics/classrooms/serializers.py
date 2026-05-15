from rest_framework import serializers

from apps.academics.classrooms.models import (
    Classroom
)


class ClassroomSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Classroom

        fields = [
            "id",
            "school",
            "name",
            "capacity",
            "floor",
        ]

        read_only_fields = [
            "school"
        ]