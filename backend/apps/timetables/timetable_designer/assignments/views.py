from rest_framework.views import APIView

from rest_framework.response import Response

from apps.timetables.timetable_entries.models import (
    TimetableEntry,
)

from .serializers import (

    AssignSubjectSerializer,

    AssignTeacherSerializer,

    AssignRoomSerializer,

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