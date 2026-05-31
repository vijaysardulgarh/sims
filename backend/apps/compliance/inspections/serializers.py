from rest_framework import serializers

from .models import Inspection


class InspectionSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Inspection

        fields = "__all__"