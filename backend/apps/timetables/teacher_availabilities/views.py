from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.staff.profiles.models import Staff
from apps.timetables.period_definitions.models import PeriodDefinition

from .models import TeacherAvailability
from .serializers import TeacherAvailabilityTeacherSerializer


# ==========================================================
# TEACHER LIST
# ==========================================================

class TeacherAvailabilityTeacherListView(APIView):

    def get(self, request):

        teachers = Staff.objects.filter(
            is_active=True,
            is_deleted=False,
            staff_role="Teaching",
        ).order_by(
            "employee_id",
        )

        serializer = TeacherAvailabilityTeacherSerializer(
            teachers,
            many=True,
        )

        return Response(serializer.data)


# ==========================================================
# BULK MATRIX
# ==========================================================

class TeacherAvailabilityBulkMatrixView(APIView):

    def get(self, request):

        teacher_id = request.query_params.get("teacher")

        if not teacher_id:
            return Response(
                {"detail": "Teacher is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        teacher = Staff.objects.filter(
            pk=teacher_id,
            is_active=True,
            is_deleted=False,
        ).first()

        if not teacher:
            return Response(
                {"detail": "Teacher not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        periods = PeriodDefinition.objects.filter(
            is_active=True,
            is_deleted=False,
        ).order_by(
            "display_order",   # ✅ Correct field
        )

        existing = TeacherAvailability.objects.filter(
            teacher=teacher,
            is_deleted=False,
        )

        availability_map = {
            (item.day, item.period_id): item.is_available
            for item in existing
        }

        days = [
            "MON",
            "TUE",
            "WED",
            "THU",
            "FRI",
            "SAT",
        ]

        matrix = {}

        for day in days:

            matrix[day] = {}

            for period in periods:

                matrix[day][period.id] = availability_map.get(
                    (day, period.id),
                    True,
                )

        return Response(matrix)


# ==========================================================
# BULK SAVE
# ==========================================================

class TeacherAvailabilityBulkSaveView(APIView):

    @transaction.atomic
    def post(self, request):

        teacher_id = request.data.get("teacher")
        availability = request.data.get("availability", [])

        if not teacher_id:
            return Response(
                {"detail": "Teacher is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        teacher = Staff.objects.filter(
            pk=teacher_id,
            is_active=True,
            is_deleted=False,
        ).first()

        if not teacher:
            return Response(
                {"detail": "Teacher not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        for row in availability:

            TeacherAvailability.objects.update_or_create(

                school=teacher.school,
                academic_session=teacher.academic_session,
                teacher=teacher,
                day=row["day"],
                period_id=row["period"],

                defaults={
                    "is_available": row["is_available"],
                },
            )

        return Response(
            {
                "message": "Availability saved successfully.",
            },
            status=status.HTTP_200_OK,
        )