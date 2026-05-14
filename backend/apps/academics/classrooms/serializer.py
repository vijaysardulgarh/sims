from rest_framework import serializers

from apps.academics.classrooms import (
    Classroom
)


class ClassroomSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Classroom

        fields = "__all__"

        read_only_fields = [
            "school"
        ]