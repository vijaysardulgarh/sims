from django.db.models import (
    Avg,
    Max,
    Min,
    Count,
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.core.views.base_views import (
    BaseAPIView
)

from apps.students.students.models import (
    Student
)

from apps.exams.exams.models import (
    Exam
)

from apps.exams.result_generations.models import (
    ResultGeneration
)


class AnalyticsAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        *args,
        **kwargs
    ):

        school = self.get_school()

        total_students = (
            Student.objects.filter(
                school=school,
                is_deleted=False,
            ).count()
        )

        total_exams = (
            Exam.objects.filter(
                school=school,
                is_deleted=False,
            ).count()
        )

        results = (
            ResultGeneration.objects.filter(
                school=school,
                is_deleted=False,
            )
        )

        total_results = results.count()

        pass_count = (
            results.filter(
                result_status="PASS"
            ).count()
        )

        fail_count = (
            results.filter(
                result_status="FAIL"
            ).count()
        )

        pass_percentage = 0

        fail_percentage = 0

        if total_results:

            pass_percentage = round(
                (
                    pass_count
                    /
                    total_results
                ) * 100,
                2,
            )

            fail_percentage = round(
                (
                    fail_count
                    /
                    total_results
                ) * 100,
                2,
            )

        aggregate = results.aggregate(

            average_score=Avg(
                "percentage"
            ),

            highest_score=Max(
                "percentage"
            ),

            lowest_score=Min(
                "percentage"
            ),
        )

        data = {

            "total_students":
                total_students,

            "total_exams":
                total_exams,

            "pass_percentage":
                pass_percentage,

            "fail_percentage":
                fail_percentage,

            "average_score":
                aggregate[
                    "average_score"
                ] or 0,

            "highest_score":
                aggregate[
                    "highest_score"
                ] or 0,

            "lowest_score":
                aggregate[
                    "lowest_score"
                ] or 0,
        }

        return self.success_response(
            data=data
        )