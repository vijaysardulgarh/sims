from django.db import transaction

from rest_framework.views import APIView

from rest_framework.response import Response

from apps.timetables.period_definitions.models import (
    PeriodDefinition,
)

from apps.timetables.timetable_entries.models import (
    TimetableEntry,
)

from .serializers import (
    MoveEntrySerializer,
)


class MoveEntryView(
    APIView
):

    @transaction.atomic
    def post(
        self,
        request
    ):

        serializer = (
            MoveEntrySerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = (
            serializer.validated_data
        )

        source_entry = (

            TimetableEntry.objects.get(
                id=data["entry_id"]
            )

        )

        target_period = (

            PeriodDefinition.objects.get(
                display_order=data["period"]
            )

        )

        target_entry = (

            TimetableEntry.objects.filter(

                timetable=
                source_entry.timetable,

                day=
                data["day"],

                period=
                target_period,

            ).first()

        )

        if target_entry:

            source_day = (
                source_entry.day
            )

            source_period = (
                source_entry.period
            )

            # temporary move
            source_entry.day = "SUN"
            source_entry.save()

            target_entry.day = (
                source_day
            )

            target_entry.period = (
                source_period
            )

            target_entry.save()

        source_entry.day = (
            data["day"]
        )

        source_entry.period = (
            target_period
        )

        source_entry.save()

        return Response(
            {
                "success": True
            }
        )