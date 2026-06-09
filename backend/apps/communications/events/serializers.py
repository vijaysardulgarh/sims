from rest_framework import serializers

from .models import Event


class EventSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Event

        fields = "__all__"

        read_only_fields = [

            "school",

            "created_at",
            "updated_at",

            "created_by",
            "updated_by",
        ]