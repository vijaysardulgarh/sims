from rest_framework import serializers

from .models import Room


class RoomSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    building_name = serializers.CharField(
        source="building.name",
        read_only=True
    )

    floor_name = serializers.CharField(
        source="floor.name",
        read_only=True
    )

    class Meta:

        model = Room

        fields = "__all__"