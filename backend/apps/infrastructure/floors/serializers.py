from rest_framework import serializers

from .models import Floor


class FloorSerializer(
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

    class Meta:

        model = Floor

        fields = "__all__"