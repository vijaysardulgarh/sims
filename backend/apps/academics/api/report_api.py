from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import (
    Count,
    Q,
    Case,
    When
)

from apps.core.utils.helpers import (
    get_current_school
)

from apps.students.models import Student

from apps.academics.models import (
    ClassSubject
)


# =========================================
# SUBJECT STRENGTH REPORT
# =========================================

class SubjectStrengthAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)

        if not school:
            return Response(
                {"error": "School not selected"},
                status=400
            )

        class_order = {
            "Sixth": 1,
            "Seventh": 2,
            "Eighth": 3,
            "Nineth": 4,
            "Tenth": 5,
            "Eleventh": 6,
            "Twelfth": 7,
        }

        data = list(

            Student.objects.filter(
                school_name=school.name
            )

            .values(
                "studentclass",
                "section",
                "stream"
            )

            .annotate(

                punjabi=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Punjabi"
                    )
                ),

                english=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="English"
                    )
                ),

                mathematics=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Mathematics"
                    )
                ),

                science=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Science"
                    )
                ),

                physics=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Physics"
                    )
                ),

                chemistry=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Chemistry"
                    )
                ),

                biology=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Biology"
                    )
                ),

                computer_science=Count(
                    "srn",
                    filter=Q(
                        subjects_opted__icontains="Computer Science"
                    )
                ),

                order=Case(
                    *[
                        When(
                            studentclass=cls,
                            then=pos
                        )
                        for cls, pos in class_order.items()
                    ]
                )
            )

            .order_by("order")
        )

        return Response(data)


# =========================================
# SUBJECTS OFFERED REPORT
# =========================================

class SubjectsOfferedAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)

        if not school:
            return Response(
                {"error": "School not selected"},
                status=400
            )

        class_subjects = (

            ClassSubject.objects

            .select_related(
                "class_obj",
                "stream",
                "subject"
            )

            .filter(
                class_obj__school=school
            )

            .order_by(
                "class_obj__name",
                "subject__name"
            )
        )

        grouped_data = {}

        for cs in class_subjects:

            class_name = cs.class_obj.name

            if cs.stream:
                class_name += f" - {cs.stream.name}"

            if cs.sub_stream:
                class_name += f" - {cs.sub_stream}"

            grouped_data.setdefault(
                class_name,
                []
            )

            grouped_data[class_name].append({

                "subject":
                    cs.subject.name,

                "periods_per_week":
                    cs.periods_per_week,

                "is_optional":
                    cs.is_optional,

                "has_lab":
                    cs.has_lab,
            })

        return Response(grouped_data)