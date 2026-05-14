from rest_framework import viewsets

from apps.academics.days import (
    Day
)

from apps.academics.days.serializer import (
    DaySerializer
)


class DayViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Day.objects.all()
    )

    serializer_class = (
        DaySerializer
    )