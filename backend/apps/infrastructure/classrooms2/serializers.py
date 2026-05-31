from rest_framework import serializers

from .models import Classroom


class ClassroomSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(

        source="school.name",

        read_only=True
    )

    room_name = serializers.CharField(

        source="room.room_name",

        read_only=True
    )

    room_number = serializers.CharField(

        source="room.room_number",

        read_only=True
    )

    class Meta:

        model = Classroom

        fields = "__all__"