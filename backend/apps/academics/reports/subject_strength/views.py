from django.db.models import (
    Case,
    When,
    IntegerField
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.students.models import (
    Student
)

from apps.academics.curriculum.subjects.models import (
    Subject
)

from apps.core.common.views import (
    BaseAPIView
)


# ==========================================
# SUBJECT STRENGTH API VIEW
# ==========================================

class SubjectStrengthAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # ======================================
    # GET
    # ======================================

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        # ==================================
        # SCHOOL CHECK
        # ==================================

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        # ==================================
        # CLASS ORDER
        # ==================================

        class_order = {

            "Sixth": 1,

            "Seventh": 2,

            "Eighth": 3,

            "Ninth": 4,

            "Tenth": 5,

            "Eleventh": 6,

            "Twelfth": 7,
        }

        # ==================================
        # SUBJECTS
        # ==================================

        subjects = (

            Subject.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("name")
        )

        # ==================================
        # STUDENT GROUPS
        # ==================================

        student_groups = (

            Student.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .values(

                "studentclass",

                "section",

                "stream",
            )

            .annotate(

                order=Case(

                    *[

                        When(

                            studentclass=cls,

                            then=pos
                        )

                        for cls, pos in (
                            class_order.items()
                        )
                    ],

                    output_field=IntegerField()
                )
            )

            .order_by("order")
        )

        # ==================================
        # FINAL DATA
        # ==================================

        final_data = []

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

            base_queryset = (

                Student.objects.filter(

                    school=school,

                    studentclass=group[
                        "studentclass"
                    ],

                    section=group[
                        "section"
                    ],

                    stream=group[
                        "stream"
                    ],

                    is_active=True,

                    is_deleted=False
                )
            )

            # ==============================
            # SUBJECT COUNTS
            # ==============================

            for subject in subjects:

                count = (

                    base_queryset.filter(

                        subjects_opted__icontains=
                        subject.name

                    ).count()
                )

                row["subjects"][
                    subject.name
                ] = count

            final_data.append(
                row
            )

        # ==================================
        # RESPONSE
        # ==================================

        return self.success_response(
            data=final_data
        )