from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.timetable.days.models import (
    Day
)

from apps.academics.timetable.days.serializers import (
    DaySerializer
)


class DayViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        DaySerializer
    )

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "sequence",
        "name"
    ]

    filterset_fields = [
        "sequence"
    ]

    def get_queryset(self):

        queryset = (
            Day.objects.all()
        )

        return self.filter_queryset_by_school(
            queryset
        )