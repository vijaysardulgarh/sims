from django.db.models import (
    Count
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.academics.timetable.timetables.models import (
    Timetable
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.academics.reports.teacher_workload.serializers import (
    TeacherWorkloadSerializer
)


# ==========================================
# TEACHER WORKLOAD API VIEW
# ==========================================

class TeacherWorkloadAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # ======================================
    # GET
    # ======================================

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        # ==================================
        # SCHOOL CHECK
        # ==================================

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        # ==================================
        # QUERYSET
        # ==================================

        queryset = (

            Timetable.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False
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

        # ==================================
        # SERIALIZER
        # ==================================

        serializer = (

            TeacherWorkloadSerializer(

                queryset,

                many=True
            )
        )

        # ==================================
        # RESPONSE
        # ==================================

        return self.success_response(
            data=serializer.data
        )