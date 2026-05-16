from django.db.models import (
    Count
)

from apps.academics.timetables.models import (
    Timetable
)

from apps.academics.reports.common.base_api import (
    BaseReportAPIView
)

from apps.academics.reports.teacher_workload.serializers import (
    TeacherWorkloadSerializer
)


class TeacherWorkloadAPIView(
    BaseReportAPIView
):

    def get(self, request):

        school = self.get_school(
            request
        )

        if not school:

            return (
                self.school_error_response()
            )

        queryset = (

            Timetable.objects

            .filter(
                school=school
            )

            .values(

                "teacher_subject_assignment"
                "__teacher__id",

                "teacher_subject_assignment"
                "__teacher__name",
            )

            .annotate(
                total_periods=Count("id")
            )

            .order_by(
                "-total_periods"
            )
        )

        serializer = (

            TeacherWorkloadSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            serializer.data
        )