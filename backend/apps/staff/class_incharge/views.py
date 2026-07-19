from django.db.models import Count

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.students.profiles.models import Student
from apps.staff.class_incharge.models import ClassIncharge

from .serializers import ClassInchargeSerializer


# ==========================================================
# CRUD API
# ==========================================================

class ClassInchargeViewSet(viewsets.ModelViewSet):

    queryset = (
        ClassIncharge.objects
        .select_related(
            "section",
            "section__class_obj",
            "section__stream",
            "section__medium",
            "staff",
        )
        .order_by(
            "section__class_obj__display_order",
            "section__name",
        )
    )

    serializer_class = ClassInchargeSerializer


# ==========================================================
# REPORT API
# ==========================================================

class ClassInchargeReportAPIView(APIView):

    def get(self, request):

        student_strength = (
            Student.objects
            .values(
                "student_class",
                "section",
            )
            .annotate(
                strength=Count("srn")
            )
        )

        strength_lookup = {
            (
                item["student_class"],
                item["section"],
            ): item["strength"]
            for item in student_strength
        }

        incharges = (
            ClassIncharge.objects
            .filter(active=True)
            .select_related(
                "section",
                "section__class_obj",
                "section__stream",
                "section__medium",
                "staff",
            )
            .order_by(
                "section__class_obj__display_order",
                "section__name",
            )
        )

        results = []

        for obj in incharges:

            section = obj.section
            teacher = obj.staff

            strength = strength_lookup.get(
                (
                    section.class_obj_id,
                    section.id,
                ),
                0,
            )

            results.append({

                "id": obj.id,

                "class": (
                    section.class_obj.name
                    if section.class_obj else ""
                ),

                "section": section.name,

                "stream": (
                    section.stream.name
                    if section.stream else ""
                ),

                "sub_stream": (
                    section.sub_stream or ""
                ),

                "medium": (
                    section.medium.name
                    if section.medium else ""
                ),

                "teacher_id": teacher.id,

                "employee_id": teacher.employee_id,

                "teacher_name": teacher.name,

                "designation": teacher.designation,

                "mobile_number": teacher.mobile_number,

                "email": teacher.email,

                "contact": (
                    teacher.mobile_number
                    or teacher.email
                    or ""
                ),

                "student_strength": strength,

                "assigned_date": obj.assigned_date,

                "effective_from": obj.effective_from,

                "effective_to": obj.effective_to,

                "remarks": obj.remarks,

                "active": obj.active,

            })

        return Response(results)