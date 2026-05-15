from django.db.models import (
    Count
)

from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from apps.academics.timetables import (
    Timetable
)

from backend.apps.academics.reports.teacher_workload.serializers import (
    TeacherWorkloadSerializer
)


class TeacherWorkloadAPIView(
    APIView
):

    def get(self, request):

        queryset = (

            Timetable.objects

            .values(
                "teacher_subject_assignment__teacher__name"
            )

            .annotate(
                total=Count("id")
            )
        )

        serializer = (

            TeacherWorkloadSerializer(
                queryset,
                many=True
            )
        )

        return Response(
            serializer.data
        )