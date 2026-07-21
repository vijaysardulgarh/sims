from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from apps.staff.profiles.models import Staff
from apps.timetables.period_definitions.models import PeriodDefinition

from .models import TeacherAvailability
from .serializers import TeacherAvailabilityTeacherSerializer
from apps.academics.sessions.models import AcademicSession

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
            "display_order",
        )

        existing = TeacherAvailability.objects.filter(
            teacher=teacher,
            is_deleted=False,
        )

        availability_map = {
            (item.day, item.period_id): item.is_available
            for item in existing
        }

        # Included Sunday to match your frontend model
        days = [
            "MON",
            "TUE",
            "WED",
            "THU",
            "FRI",
            "SAT",
            "SUN", 
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

        # 1. Fetch the currently active academic session
        current_session = AcademicSession.objects.filter(is_current=True).first()
        
        if not current_session:
            return Response(
                {"detail": "No active academic session found in the system."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        availability_instances = []
        
        for row in availability:
            availability_instances.append(
                TeacherAvailability(
                    school=teacher.school,
                    academic_session=current_session,  # 2. Replaced teacher.academic_session
                    teacher=teacher,
                    day=row["day"],
                    period_id=row["period"],
                    is_available=row["is_available"]
                )
            )

        if availability_instances:
            TeacherAvailability.objects.bulk_create(
                availability_instances,
                update_conflicts=True,
                unique_fields=['school', 'academic_session', 'teacher', 'day', 'period'],
                update_fields=['is_available']
            )

        return Response(
            {"message": "Availability saved successfully."},
            status=status.HTTP_200_OK,
        )