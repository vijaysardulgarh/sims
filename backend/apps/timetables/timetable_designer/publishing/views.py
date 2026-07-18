from rest_framework.views import APIView

from rest_framework.response import Response

from apps.timetables.timetables.models import (
    Timetable,
)

from .serializers import (

    PublishTimetableSerializer,

    CompareVersionSerializer,

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