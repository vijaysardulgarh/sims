from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q, Case, When

from apps.core.utils import get_current_school
from apps.students.models import Student, StudentAchievement


# =========================================
# ACHIEVEMENT LIST
# =========================================
class AchievementListAPIView(APIView):

    def get(self, request):
        achievements = StudentAchievement.objects.select_related("exam_detail").all().order_by("-date")

        data = [
            {
                "id": a.id,
                "date": a.date,
                "exam": a.exam_detail.name if a.exam_detail else None,
            }
            for a in achievements
        ]

        return Response(data)


# =========================================
# ACHIEVEMENT DETAIL
# =========================================
class AchievementDetailAPIView(APIView):

    def get(self, request, pk):
        achievement = get_object_or_404(
            StudentAchievement.objects.select_related("exam_detail"),
            pk=pk
        )

        return Response({
            "id": achievement.id,
            "date": achievement.date,
            "exam": achievement.exam_detail.name if achievement.exam_detail else None,
        })


# =========================================
# STUDENT STRENGTH (FULL ORIGINAL LOGIC)
# =========================================
class StudentStrengthAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        class_order = {
            "Sixth": 1, "Seventh": 2, "Eighth": 3, "Nineth": 4,
            "Tenth": 5, "Eleventh": 6, "Twelfth": 7,
        }

        data = list(
            Student.objects.filter(school_name=school.name)
            .values("studentclass", "section", "stream")
            .annotate(
                scmale=Count("srn", filter=Q(gender="Male", category__in=["SC", "Scheduled Caste"])),
                scfemale=Count("srn", filter=Q(gender="Female", category__in=["SC", "Scheduled Caste"])),

                bcamale=Count("srn", filter=Q(gender="Male", category="BC-A")),
                bcafemale=Count("srn", filter=Q(gender="Female", category="BC-A")),

                bcbmale=Count("srn", filter=Q(gender="Male", category="BC-B")),
                bcbfemale=Count("srn", filter=Q(gender="Female", category="BC-B")),

                genmale=Count("srn", filter=Q(gender="Male", category="GEN")),
                genfemale=Count("srn", filter=Q(gender="Female", category="GEN")),

                totalmale=Count("srn", filter=Q(gender="Male")),
                totalfemale=Count("srn", filter=Q(gender="Female")),
                total=Count("srn"),

                malecwsn=Count("srn", filter=Q(gender="Male") & ~Q(disability=None) & ~Q(disability="")),
                femalecwsn=Count("srn", filter=Q(gender="Female") & ~Q(disability=None) & ~Q(disability="")),
                cwsn=Count("srn", filter=~Q(disability="") | ~Q(disability=None)),

                malebpl=Count("srn", filter=Q(gender="Male") & ~Q(bpl_certificate_issuing_authority=None) & ~Q(bpl_certificate_issuing_authority="")),
                femalebpl=Count("srn", filter=Q(gender="Female") & ~Q(bpl_certificate_issuing_authority=None) & ~Q(bpl_certificate_issuing_authority="")),
                bpl=Count("srn", filter=~Q(bpl_certificate_issuing_authority="") | ~Q(bpl_certificate_issuing_authority=None)),

                order=Case(*[When(studentclass=cls, then=pos) for cls, pos in class_order.items()])
            )
            .order_by("order")
        )

        return Response(data)