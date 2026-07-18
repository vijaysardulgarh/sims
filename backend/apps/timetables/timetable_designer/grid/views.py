from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    AllowAny,
)

from apps.timetables.timetable_entries.models import (
    TimetableEntry,
)

from .serializers import (
    TimetableGridSerializer,
)



from rest_framework.permissions import (
    AllowAny,
)
class TimetableGridView(
    APIView
):

    permission_classes = [
        AllowAny
    ]
    def get(
        self,
        request,
        timetable_id
    ):

        queryset = (

            TimetableEntry.objects

            .filter(
                timetable_id=timetable_id
            )

            .select_related(
                "subject",
                "teacher",
                "period"
            )

        )

        serializer = (

            TimetableGridSerializer(
                queryset,
                many=True
            )

        )

        return Response(
            serializer.data
        )




class TeacherView(
    APIView
):

    def get(
        self,
        request,
        teacher_id
    ):

        entries = (

            TimetableEntry.objects.filter(
                teacher_id=
                teacher_id
            )

        )

        data = [

            {

                "id":
                    entry.id,

                "day":
                    entry.day,

                "period":
                    entry.period_id,

            }

            for entry in entries

        ]

        return Response(
            data
        )


class RoomView(
    APIView
):

    def get(
        self,
        request,
        room_id
    ):

        entries = (

            TimetableEntry.objects.filter(
                room_id=
                room_id
            )

        )

        data = [

            {

                "id":
                    entry.id,

                "day":
                    entry.day,

                "period":
                    entry.period_id,

            }

            for entry in entries

        ]

        return Response(
            data
        )


class ClassView(
    APIView
):

    def get(
        self,
        request,
        class_id
    ):

        entries = (

            TimetableEntry.objects.filter(
                school_class_id=
                class_id
            )

        )

        data = [

            {

                "id":
                    entry.id,

                "day":
                    entry.day,

                "period":
                    entry.period_id,

            }

            for entry in entries

        ]

        return Response(
            data
        )