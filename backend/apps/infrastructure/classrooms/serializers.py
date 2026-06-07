from rest_framework import serializers

from apps.infrastructure.classrooms.models import (
    Classroom
)


class ClassroomSerializer(
    serializers.ModelSerializer
):

    room_name = serializers.CharField(
        source="room.room_name",
        read_only=True
    )

    room_number = serializers.CharField(
        source="room.room_number",
        read_only=True
    )

    floor_name = serializers.CharField(
        source="floor.name",
        read_only=True
    )

    class Meta:

        model = Classroom

        fields = [

            "id",

            "room",
            "room_name",
            "room_number",

            "floor",
            "floor_name",

            "classroom_code",

            "capacity",

            "description",

            "smart_classroom",

            "air_conditioned",

            "projector_available",

            "whiteboard_available",

            "internet_enabled",

            "is_active",

            "created_at",
            "updated_at",
        ]

        read_only_fields = [

            "id",

            "created_at",

            "updated_at",
        ]