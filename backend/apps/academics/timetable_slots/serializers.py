from rest_framework import serializers

from apps.academics.timetable_slots.models import (
    TimetableSlot
)


class TimetableSlotSerializer(
    serializers.ModelSerializer
):

    day_name = serializers.CharField(
        source="day.name",
        read_only=True
    )

    class Meta:

        model = TimetableSlot

        fields = "__all__"