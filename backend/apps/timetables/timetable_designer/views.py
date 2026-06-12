from rest_framework import status

from rest_framework.views import APIView

from rest_framework.response import Response

from apps.timetables.timetables.models import (
    Timetable
)

from apps.timetables.timetable_entries.models import (
    TimetableEntry
)

from .serializers import (
    GenerateTimetableSerializer,
    MoveEntrySerializer,
    CopyDaySerializer,
    CopyWeekSerializer,
    PublishTimetableSerializer,
    CompareVersionSerializer
)


class GenerateTimetableView(
    APIView
):

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

        return Response(

            {
                "success": True,
                "message":
                    "Timetable generated successfully."
            },

            status=
            status.HTTP_200_OK

        )


class MoveEntryView(
    APIView
):

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

        entry = (
            TimetableEntry.objects.get(
                id=data["entry_id"]
            )
        )

        entry.day = (
            data["day"]
        )

        entry.period_id = (
            data["period"]
        )

        entry.save()

        return Response(

            {
                "success": True
            }

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


class PublishTimetableView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            PublishTimetableSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        timetable = (
            Timetable.objects.get(
                id=
                serializer.validated_data[
                    "timetable"
                ]
            )
        )

        timetable.is_published = True

        timetable.save()

        return Response(

            {
                "success": True
            }

        )


class ConflictCheckView(
    APIView
):

    def get(
        self,
        request
    ):

        conflicts = []

        return Response(
            conflicts
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


class CompareVersionView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            CompareVersionSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response(

            {
                "differences": []
            }

        )

class TimetableGridView(
    APIView
):

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
                "room",
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

class AssignSubjectView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            AssignSubjectSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = (
            serializer.validated_data
        )

        entry = (
            TimetableEntry.objects.get(
                id=data["entry_id"]
            )
        )

        entry.subject_id = (
            data["subject_id"]
        )

        entry.save()

        return Response(

            {
                "success": True
            }

        )

class AssignTeacherView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            AssignTeacherSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = (
            serializer.validated_data
        )

        entry = (
            TimetableEntry.objects.get(
                id=data["entry_id"]
            )
        )

        entry.teacher_id = (
            data["teacher_id"]
        )

        entry.save()

        return Response(

            {
                "success": True
            }

        )

class AssignRoomView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            AssignRoomSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = (
            serializer.validated_data
        )

        entry = (
            TimetableEntry.objects.get(
                id=data["entry_id"]
            )
        )

        entry.room_id = (
            data["room_id"]
        )

        entry.save()

        return Response(

            {
                "success": True
            }

        )                                