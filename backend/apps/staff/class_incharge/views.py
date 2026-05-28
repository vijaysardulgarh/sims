from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.students.profiles.models import Student
from apps.staff.class_incharge.models import ClassIncharge


class ClassInchargeReportAPIView(APIView):

    def get(self, request):

        # ============================================
        # STUDENT STRENGTH
        # ============================================

        student_counts = (
            Student.objects.values(
                "student_class",
                "section"
            )
            .annotate(
                strength=Count("srn")
            )
        )

        strength_lookup = {

            (
                s["student_class"],
                s["section"]
            ): s["strength"]

            for s in student_counts
        }

        # ============================================
        # ACTIVE INCHARGES
        # ============================================

        incharges = (
            ClassIncharge.objects
            .filter(active=True)
            .select_related(
                "section__class_obj",
                "section__stream",
                "section__medium",
                "staff"
            )
        )

        data = []

        # ============================================
        # RESPONSE DATA
        # ============================================

        for incharge in incharges:

            sec = incharge.section
            staff = incharge.staff

            key = (
                sec.class_obj_id,
                sec.id
            )

            strength = strength_lookup.get(key, 0)

            data.append({

                "id": incharge.id,

                "class": (
                    sec.class_obj.name
                    if sec.class_obj else ""
                ),

                "section": sec.name,

                "stream": (
                    sec.stream.name
                    if sec.stream else ""
                ),

                "sub_stream": (
                    sec.sub_stream or ""
                ),

                "medium": (
                    sec.medium.name
                    if sec.medium else ""
                ),

                "teacher": staff.name,

                "contact": (
                    staff.mobile_number
                    or staff.email
                    or ""
                ),

                "student_strength": strength,

                "effective_from":
                    incharge.effective_from,

                "effective_to":
                    incharge.effective_to,

                "active":
                    incharge.active,
            })

        return Response(data)