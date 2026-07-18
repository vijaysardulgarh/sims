from rest_framework import status

from rest_framework.views import APIView

from rest_framework.response import Response

from apps.timetables.period_definitions.models import (
    PeriodDefinition,
)

from apps.timetables.timetables.models import (
    Timetable,
)

from apps.timetables.timetable_entries.models import (
    TimetableEntry,
)

from .serializers import (

    GenerateTimetableSerializer,

    CopyDaySerializer,

    CopyWeekSerializer,

)

class GenerateTimetableView(
    APIView
):

    DAYS = [

        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",

    ]

    def post(
        self,
        request
    ):

        serializer = (
            GenerateTimetableSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        timetable_id = (
            serializer.validated_data[
                "timetable"
            ]
        )

        timetable = (
            Timetable.objects.get(
                id=timetable_id
            )
        )

        periods = (

            PeriodDefinition.objects.filter(

                # school=
                # timetable.school,

                # academic_session=
                # timetable.academic_session,

                is_active=True,

            )

            .order_by(
                "display_order"
            )

        )

        created_count = 0

        for day in self.DAYS:

            for period in periods:

                print(
                    "PERIOD COUNT:",
                    periods.count()
                )

                print(
                    day,
                    period.id
                )

                _, created = (

                    TimetableEntry.objects.get_or_create(

                        timetable=
                        timetable,

                        day=
                        day,

                        period=
                        period,

                        defaults={

                            "remarks": "",

                        }

                    )

                )

                if created:

                    created_count += 1

        return Response(

            {
                "success": True,

                "created_entries":
                    created_count,

                "total_entries":
                    TimetableEntry.objects.filter(
                        timetable=timetable
                    ).count(),

                "message":
                    "Timetable generated successfully."

            },

            status=
            status.HTTP_200_OK

        )


class CopyDayView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            CopyDaySerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = (
            serializer.validated_data
        )

        source_entries = (

            TimetableEntry.objects.filter(

                timetable_id=
                data["timetable"],

                day=
                data["source_day"]

            )

        )

        for entry in source_entries:

            entry.pk = None

            entry.day = (
                data["target_day"]
            )

            entry.save()

        return Response(

            {
                "success": True
            }

        )


class CopyWeekView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            CopyWeekSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response(

            {
                "success": True,
                "message":
                    "Week copied successfully."
            }

        )