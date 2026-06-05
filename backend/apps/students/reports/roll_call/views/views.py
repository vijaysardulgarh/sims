from rest_framework.views import APIView
from rest_framework.response import Response

from apps.students.profiles.models import Student

from ..serializers.serializers import (
    RollCallSerializer,
)


class RollCallFiltersAPIView(APIView):

    def get(self, request):

        school = request.user.school

        classes = (

            Student.objects

            .filter(
                school=school
            )

            .values_list(
                "student_class__name",
                flat=True
            )

            .distinct()

        )

        sections = (

            Student.objects

            .filter(
                school=school
            )

            .values_list(
                "section__name",
                flat=True
            )

            .distinct()

        )

        return Response({

            "classes": sorted(
                list(
                    filter(
                        None,
                        classes
                    )
                )
            ),

            "sections": sorted(
                list(
                    filter(
                        None,
                        sections
                    )
                )
            ),

        })

class RollCallAPIView(APIView):

    def get(self, request):

        school = request.user.school

        class_name = request.GET.get(
            "class",
        )

        section_name = request.GET.get(
            "section",
        )

        students = (
            Student.objects
            .filter(
                school=request.user.school,
                student_class__name=class_name,
                section__name=section_name,
            )
            .order_by(
                "roll_number",
            )
        )

        serializer = RollCallSerializer(
            students,
            many=True,
        )

        return Response({

            "school_name": school.name,

            "school_address": getattr(
                school,
                "address",
                "",
            ),

            "class_name": class_name,

            "section_name": section_name,

            "total_students": students.count(),

            "students": serializer.data,

        })