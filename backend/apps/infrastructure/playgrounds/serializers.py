from rest_framework import serializers

from .models import Playground


class PlaygroundSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Playground

        fields = "__all__"