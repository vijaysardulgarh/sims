from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.staff.profiles.models import Staff
from apps.staff.teacher_attendance.models import TeacherAttendance


class TeacherAttendanceAPIView(APIView):
    """
    GET  : Load teacher attendance for a selected date
    POST : Save bulk teacher attendance
    """

    def get(self, request):

        date_str = request.GET.get("date")

        attendance_date = (
            parse_date(date_str)
            if date_str
            else timezone.now().date()
        )

        if attendance_date is None:
            return Response(
                {
                    "error": "Invalid attendance date."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        teachers = (
            Staff.objects.filter(
                staff_role="Teaching",
                is_active=True,
            )
            .select_related("post_type")
            .order_by("employee_id")
        )

        attendance_map = {
            attendance.teacher_id: attendance
            for attendance in TeacherAttendance.objects.filter(
                date=attendance_date,
            ).select_related("teacher")
        }

        data = []

        for teacher in teachers:

            attendance = attendance_map.get(teacher.id)

            data.append(
                {
                    "teacher": teacher.id,
                    "employee_id": teacher.employee_id,
                    "teacher_name": teacher.name,
                    "post_type": (
                        teacher.post_type.name
                        if teacher.post_type
                        else ""
                    ),
                    "date": attendance_date,
                    "status": (
                        attendance.status
                        if attendance
                        else TeacherAttendance.PRESENT
                    ),
                    "remarks": (
                        attendance.remarks
                        if attendance
                        else ""
                    ),
                    "check_in": (
                        attendance.check_in
                        if attendance
                        else None
                    ),
                    "check_out": (
                        attendance.check_out
                        if attendance
                        else None
                    ),
                }
            )

        return Response(
            {
                "date": attendance_date,
                "teachers": data,
            }
        )

    def post(self, request):

        attendance_date = parse_date(
            request.data.get("date")
        )

        if attendance_date is None:
            return Response(
                {
                    "error": "Invalid attendance date."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        attendance_data = request.data.get(
            "attendance",
            [],
        )

        if not attendance_data:
            return Response(
                {
                    "error": "No attendance data received."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():

            for item in attendance_data:

                teacher = get_object_or_404(
                    Staff,
                    pk=item.get("teacher"),
                    staff_role="Teaching",
                )

                TeacherAttendance.objects.update_or_create(
                    teacher=teacher,
                    date=attendance_date,
                    defaults={
                        "status": item.get(
                            "status",
                            TeacherAttendance.PRESENT,
                        ),
                        "remarks": item.get(
                            "remarks",
                            "",
                        ),
                        "check_in": item.get(
                            "check_in",
                        ),
                        "check_out": item.get(
                            "check_out",
                        ),
                    },
                )

        return Response(
            {
                "message": "Attendance saved successfully.",
                "date": attendance_date,
                "total": len(attendance_data),
            },
            status=status.HTTP_200_OK,
        )


class TeacherAttendanceUpdateAPIView(APIView):
    """
    Update a single attendance record
    """

    def put(self, request, pk):

        attendance = get_object_or_404(
            TeacherAttendance,
            pk=pk,
        )

        attendance.status = request.data.get(
            "status",
            attendance.status,
        )

        attendance.remarks = request.data.get(
            "remarks",
            attendance.remarks,
        )

        attendance.check_in = request.data.get(
            "check_in",
            attendance.check_in,
        )

        attendance.check_out = request.data.get(
            "check_out",
            attendance.check_out,
        )

        attendance.save()

        return Response(
            {
                "message": "Attendance updated successfully.",
            }
        )


class TeacherAttendanceDeleteAPIView(APIView):
    """
    Delete a single attendance record
    """

    def delete(self, request, pk):

        attendance = get_object_or_404(
            TeacherAttendance,
            pk=pk,
        )

        attendance.delete()

        return Response(
            {
                "message": "Attendance deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )