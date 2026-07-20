from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.staff.profiles.models import Staff

from .models import TeacherWorkload
from .serializers import TeacherWorkloadSerializer


class TeacherWorkloadListView(APIView):

    def get(self, request):

        teachers = (
            Staff.objects.filter(
                is_deleted=False,
            )
            .order_by("name")
        )

        data = []

        for teacher in teachers:

            workload = (
                TeacherWorkload.objects.filter(
                    teacher=teacher,
                    is_deleted=False,
                )
                .first()
            )

            if workload:

                data.append(
                    TeacherWorkloadSerializer(
                        workload
                    ).data
                )

            else:

                data.append(
                    {
                        "id": None,
                        "teacher": teacher.id,
                        "teacher_name": teacher.name,
                        "employee_id": teacher.employee_id,
                        "max_periods_per_day": 6,
                        "min_periods_per_day": 0,
                        "max_periods_per_week": 36,
                        "min_periods_per_week": 0,
                        "max_consecutive_periods": 3,
                    }
                )

        return Response(data)


class TeacherWorkloadBulkSaveView(APIView):

    @transaction.atomic
    def post(self, request):

        for row in request.data:

            workload, created = (
                TeacherWorkload.objects.update_or_create(
                    teacher_id=row["teacher"],
                    defaults={
                        "max_periods_per_day": row["max_periods_per_day"],
                        "min_periods_per_day": row["min_periods_per_day"],
                        "max_periods_per_week": row["max_periods_per_week"],
                        "min_periods_per_week": row["min_periods_per_week"],
                        "max_consecutive_periods": row["max_consecutive_periods"],
                        "updated_by": request.user,
                    },
                )
            )

            if created:
                workload.created_by = request.user
                workload.save(update_fields=["created_by"])

        return Response(
            {
                "message": "Teacher workloads saved successfully."
            },
            status=status.HTTP_200_OK,
        )