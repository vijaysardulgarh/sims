from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.timetable_slots.models import (
    TimetableSlot
)

from apps.academics.timetable_slots.serializers import (
    TimetableSlotSerializer
)


class TimetableSlotViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        TimetableSlotSerializer
    )

    search_fields = [
        "title",
        "day__name",
    ]

    ordering_fields = [
        "sequence_number",
        "period_number",
        "start_time",
    ]

    filterset_fields = [
        "day",
        "is_break",
        "is_assembly",
        "is_special_event",
    ]

    def get_queryset(self):

        queryset = (

            TimetableSlot.objects

            .select_related(
                "school",
                "day"
            )
        )

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            school=(
                self.request.user.school
            )
        )