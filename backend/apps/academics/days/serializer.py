from rest_framework import serializers

from apps.academics.days import (
    Day
)


class DaySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Day

        fields = "__all__"