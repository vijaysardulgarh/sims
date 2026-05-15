from django.db.models import (
    Case,
    When
)

from apps.students.models import (
    Student
)

from apps.academics.subjects import (
    Subject
)

from academics.reports.common.base_api import (
    BaseReportAPIView
)


class SubjectStrengthAPIView(
    BaseReportAPIView
):

    def get(self, request):

        school = self.get_school(
            request
        )

        if not school:

            return (
                self.school_error_response()
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

        subjects = (

            Subject.objects

            .filter(
                school=school
            )

            .order_by("name")
        )

        student_groups = (

            Student.objects

            .filter(
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

                        for cls, pos in (
                            class_order.items()
                        )
                    ]
                )
            )

            .order_by("order")
        )

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
            )

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

            final_data.append(row)

        return self.success_response(
            final_data
        )