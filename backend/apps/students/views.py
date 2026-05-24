from rest_framework.views import APIView

from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from django.db.models import (
    Count,
    Q,
    Case,
    When,
    IntegerField,
    Value,
)

from apps.students.models import (
    Student
)
from apps.students.achievements.models import (
    Achievement
)

from apps.accounts.authorization.permissions import (
    CanViewStudents
)


# =========================================
# ACHIEVEMENT LIST
# =========================================

class AchievementListAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request):

        achievements = (

            Achievement.objects

            .select_related(
                "exam_detail"
            )

            .order_by("-date")
        )

        data = [

            {
                "id": achievement.id,

                "date": achievement.date,

                "exam": (

                    achievement.exam_detail.name

                    if achievement.exam_detail

                    else None
                ),
            }

            for achievement in achievements
        ]

        return Response(data)


# =========================================
# ACHIEVEMENT DETAIL
# =========================================

class AchievementDetailAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request, pk):

        achievement = get_object_or_404(

            Achievement.objects
            .select_related("exam_detail"),

            pk=pk
        )

        data = {

            "id": achievement.id,

            "date": achievement.date,

            "exam": (

                achievement.exam_detail.name

                if achievement.exam_detail

                else None
            ),
        }

        return Response(data)


# =========================================
# STUDENT STRENGTH REPORT
# =========================================

class StudentStrengthAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request):

        # =====================================
        # CLASS ORDER
        # =====================================

        class_order = {

            "6TH": 1,
            "7TH": 2,
            "8TH": 3,
            "9TH": 4,
            "10TH": 5,
            "11TH": 6,
            "12TH": 7,
        }

        # =====================================
        # QUERYSET
        # =====================================

        queryset = (

            Student.objects.filter(
                school=request.user.school
            )

            .values(
                "student_class__name",
                "section__name",
                "stream__name",
            )

            .annotate(

                # =================================
                # SC
                # =================================

                scmale=Count(

                    "id",

                    filter=Q(
                        gender="Male",
                        category__in=[
                            "SC",
                            "Scheduled Caste"
                        ]
                    )
                ),

                scfemale=Count(

                    "id",

                    filter=Q(
                        gender="Female",
                        category__in=[
                            "SC",
                            "Scheduled Caste"
                        ]
                    )
                ),

                # =================================
                # BC-A
                # =================================

                bcamale=Count(

                    "id",

                    filter=Q(
                        gender="Male",
                        category="BC-A"
                    )
                ),

                bcafemale=Count(

                    "id",

                    filter=Q(
                        gender="Female",
                        category="BC-A"
                    )
                ),

                # =================================
                # BC-B
                # =================================

                bcbmale=Count(

                    "id",

                    filter=Q(
                        gender="Male",
                        category="BC-B"
                    )
                ),

                bcbfemale=Count(

                    "id",

                    filter=Q(
                        gender="Female",
                        category="BC-B"
                    )
                ),

                # =================================
                # GENERAL
                # =================================

                genmale=Count(

                    "id",

                    filter=Q(
                        gender="Male",
                        category="GEN"
                    )
                ),

                genfemale=Count(

                    "id",

                    filter=Q(
                        gender="Female",
                        category="GEN"
                    )
                ),

                # =================================
                # TOTAL
                # =================================

                totalmale=Count(

                    "id",

                    filter=Q(
                        gender="Male"
                    )
                ),

                totalfemale=Count(

                    "id",

                    filter=Q(
                        gender="Female"
                    )
                ),

                total=Count("id"),

                # =================================
                # CWSN
                # =================================

                malecwsn=Count(

                    "id",

                    filter=(

                        Q(gender="Male")

                        &

                        Q(
                            disability__isnull=False
                        )

                        &

                        ~Q(disability="")
                    )
                ),

                femalecwsn=Count(

                    "id",

                    filter=(

                        Q(gender="Female")

                        &

                        Q(
                            disability__isnull=False
                        )

                        &

                        ~Q(disability="")
                    )
                ),

                cwsn=Count(

                    "id",

                    filter=(

                        Q(
                            disability__isnull=False
                        )

                        &

                        ~Q(disability="")
                    )
                ),

                # =================================
                # BPL
                # =================================

                malebpl=Count(

                    "id",

                    filter=(

                        Q(gender="Male")

                        &

                        Q(
                            bpl_certificate_issuing_authority__isnull=False
                        )

                        &

                        ~Q(
                            bpl_certificate_issuing_authority=""
                        )
                    )
                ),

                femalebpl=Count(

                    "id",

                    filter=(

                        Q(gender="Female")

                        &

                        Q(
                            bpl_certificate_issuing_authority__isnull=False
                        )

                        &

                        ~Q(
                            bpl_certificate_issuing_authority=""
                        )
                    )
                ),

                bpl=Count(

                    "id",

                    filter=(

                        Q(
                            bpl_certificate_issuing_authority__isnull=False
                        )

                        &

                        ~Q(
                            bpl_certificate_issuing_authority=""
                        )
                    )
                ),

                # =================================
                # ORDER
                # =================================

                order=Case(

                    *[

                        When(
                            student_class__name=class_name,
                            then=Value(position)
                        )

                        for class_name, position

                        in class_order.items()
                    ],

                    default=Value(999),

                    output_field=IntegerField()
                )
            )

            .order_by(
                "order",
                "section__name"
            )
        )

        return Response(queryset)