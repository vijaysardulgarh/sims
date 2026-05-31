from rest_framework import serializers

from .models import Laboratory


class LaboratorySerializer(
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

    incharge_name = serializers.CharField(

        source="incharge.full_name",

        read_only=True
    )

    class Meta:

        model = Laboratory

        fields = "__all__"