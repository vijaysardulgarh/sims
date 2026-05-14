from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

from django.db.models import (
    Count,
    Q,
    Case,
    When,
)

from apps.core.utils.helpers import (
    get_current_school
)

from apps.students.models import Student

from apps.academics.models import (
    ClassSubject,
    Subject
)


# =========================================
# BASE REPORT API
# =========================================

class BaseReportAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get_school(self, request):

        return get_current_school(request)

    def school_error_response(self):

        return Response({

            "success": False,

            "message":
            "School not selected."

        }, status=400)

    def success_response(self, data):

        return Response({

            "success": True,

            "data": data
        })


# =========================================
# SUBJECT STRENGTH REPORT
# =========================================

class SubjectStrengthAPIView(
    BaseReportAPIView
):

    def get(self, request):

        school = self.get_school(request)

        if not school:
            return self.school_error_response()

        # ---------------------------------
        # CLASS ORDER
        # ---------------------------------

        class_order = {
            "Sixth": 1,
            "Seventh": 2,
            "Eighth": 3,
            "Nineth": 4,
            "Tenth": 5,
            "Eleventh": 6,
            "Twelfth": 7,
        }

        # ---------------------------------
        # GET ALL SUBJECTS
        # ---------------------------------

        subjects = Subject.objects.filter(
            school=school
        ).order_by("name")

        # ---------------------------------
        # BASE QUERY
        # ---------------------------------

        student_groups = (

            Student.objects.filter(
                school_name=school.name
            )

            .values(
                "studentclass",
                "section",
                "stream"
            )

            .annotate(

                order=Case(

                    *[
                        When(
                            studentclass=cls,
                            then=pos
                        )
                        for cls, pos
                        in class_order.items()
                    ]
                )
            )

            .order_by("order")
        )

        final_data = []

        # ---------------------------------
        # DYNAMIC SUBJECT COUNTS
        # ---------------------------------

        for group in student_groups:

            row = {

                "studentclass":
                    group["studentclass"],

                "section":
                    group["section"],

                "stream":
                    group["stream"],

                "subjects": {}
            }

            base_queryset = Student.objects.filter(

                school_name=school.name,

                studentclass=group[
                    "studentclass"
                ],

                section=group[
                    "section"
                ],

                stream=group[
                    "stream"
                ]
            )

            for subject in subjects:

                count = base_queryset.filter(

                    subjects_opted__icontains=
                    subject.name

                ).count()

                row["subjects"][
                    subject.name
                ] = count

            final_data.append(row)

        return self.success_response(
            final_data
        )


# =========================================
# SUBJECTS OFFERED REPORT
# =========================================

class SubjectsOfferedAPIView(
    BaseReportAPIView
):

    def get(self, request):

        school = self.get_school(request)

        if not school:
            return self.school_error_response()

        class_subjects = (

            ClassSubject.objects

            .select_related(
                "class_obj",
                "stream",
                "subject"
            )

            .filter(
                school=school
            )

            .order_by(
                "class_obj__class_order",
                "subject__name"
            )
        )

        grouped_data = defaultdict(list)

        for cs in class_subjects:

            class_name = (
                cs.class_obj.name
            )

            if cs.stream:
                class_name += (
                    f" - {cs.stream.name}"
                )

            if cs.sub_stream:
                class_name += (
                    f" - {cs.sub_stream}"
                )

            grouped_data[
                class_name
            ].append({

                "subject":
                    cs.subject.name,

                "theory_periods":
                    cs.theory_periods_per_week,

                "practical_periods":
                    cs.practical_periods_per_week,

                "total_periods":
                    cs.periods_per_week,

                "is_optional":
                    cs.is_optional,

                "has_lab":
                    cs.has_lab,

                "is_shared":
                    cs.is_shared,
            })

        return self.success_response(
            grouped_data
        )