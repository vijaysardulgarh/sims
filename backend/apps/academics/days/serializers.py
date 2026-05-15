from rest_framework import serializers

from apps.academics.days.models import (
    Day
)


class DaySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Day

        fields = [
            "id",
            "school",
            "name",
            "sequence",
        ]

        read_only_fields = [
            "school"
        ]