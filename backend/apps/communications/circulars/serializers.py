from rest_framework import serializers

from .models import Circular


class CircularSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Circular

        fields = "__all__"