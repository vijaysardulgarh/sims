from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.students.profiles.models import Student
from apps.staff.class_incharge.models import ClassIncharge


class ClassInchargeReportAPIView(APIView):

    def get(self, request):

        student_counts = (
            Student.objects.values(
                "studentclass",
                "section"
            )
            .annotate(
                strength=Count("srn")
            )
        )

        strength_lookup = {

            (s["studentclass"], s["section"]): s["strength"]

            for s in student_counts
        }

        incharges = (
            ClassIncharge.objects
            .filter(active=True)
            .select_related(
                "section__sec_class",
                "section__stream",
                "section__medium",
                "staff"
            )
        )

        data = []

        for incharge in incharges:

            sec = incharge.section
            staff = incharge.staff

            key = (
                sec.sec_class.name,
                sec.name
            )

            strength = strength_lookup.get(key, 0)

            data.append({
                "class": sec.sec_class.name,
                "section": sec.name,
                "stream": sec.stream.name if sec.stream else "",
                "sub_stream": sec.sub_stream or "",
                "medium": sec.medium.name if sec.medium else "",
                "teacher": staff.name,
                "contact": (
                    staff.mobile_number
                    or staff.email
                ),
                "student_strength": strength,
            })

        return Response(data)