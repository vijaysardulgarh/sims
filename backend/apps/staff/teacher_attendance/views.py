from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_date

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.staff.staff.models import (
    Staff,
)
from apps.staff.teacher_attendance.models import (
    TeacherAttendance
)

class TeacherAttendanceAPIView(APIView):

    def get(self, request):

        date_str = request.GET.get("date")

        date = (
            parse_date(date_str)
            if date_str
            else timezone.now().date()
        )

        teachers = Staff.objects.filter(
            staff_role="Teaching"
        ).order_by("name")

        attendance_records = {
            rec.teacher_id: rec
            for rec in TeacherAttendance.objects.filter(date=date)
        }

        data = []

        for teacher in teachers:

            record = attendance_records.get(teacher.id)

            data.append({
                "teacher_id": teacher.id,
                "name": teacher.name,
                "present": record.present if record else False
            })

        return Response({
            "date": date,
            "teachers": data
        })

    def post(self, request):

        date_str = request.data.get("date")

        date = (
            parse_date(date_str)
            if date_str
            else timezone.now().date()
        )

        TeacherAttendance.objects.filter(
            date=date
        ).delete()

        teachers = Staff.objects.filter(
            staff_role="Teaching"
        )

        for teacher in teachers:

            present = request.data.get(
                f"present_{teacher.id}",
                False
            )

            TeacherAttendance.objects.create(
                teacher=teacher,
                date=date,
                present=bool(present)
            )

        return Response({
            "message": "Attendance saved"
        })


class TeacherAttendanceUpdateAPIView(APIView):

    def put(self, request, pk):

        record = get_object_or_404(
            TeacherAttendance,
            pk=pk
        )

        record.present = request.data.get(
            "present",
            False
        )

        record.save()

        return Response({
            "message": "Updated"
        })


class TeacherAttendanceDeleteAPIView(APIView):

    def delete(self, request, pk):

        record = get_object_or_404(
            TeacherAttendance,
            pk=pk
        )

        record.delete()

        return Response({
            "message": "Deleted"
        })