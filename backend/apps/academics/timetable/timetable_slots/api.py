from rest_framework import viewsets

from apps.academics.timetable.timetable_slots import (
    TimetableSlot
)

from apps.academics.timetable.timetable_slots.serializers import (
    TimetableSlotSerializer
)


class TimetableSlotViewSet(
    viewsets.ModelViewSet
):

    queryset = (

        TimetableSlot.objects

        .select_related("day")
    )

    serializer_class = (
        TimetableSlotSerializer
    )