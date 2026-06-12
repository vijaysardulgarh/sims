from django.db.models import (
    Avg,
    Max,
    Min,
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.examinations.result_generations.models import (
    ResultGeneration
)


class ExamReportAPIView(
    BaseAPIView
):

    def get(
        self,
        request,
        *args,
        **kwargs
    ):

        school = self.get_school()

        queryset = (
            ResultGeneration.objects
            .filter(
                school=school,
                is_deleted=False,
            )
        )

        total_students = (
            queryset.count()
        )

        pass_count = (
            queryset.filter(
                result_status="PASS"
            ).count()
        )

        fail_count = (
            queryset.filter(
                result_status="FAIL"
            ).count()
        )

        aggregate = queryset.aggregate(

            average_percentage=Avg(
                "percentage"
            ),

            highest_percentage=Max(
                "percentage"
            ),

            lowest_percentage=Min(
                "percentage"
            ),
        )

        return self.success_response(

            data={

                "total_students":
                    total_students,

                "pass_count":
                    pass_count,

                "fail_count":
                    fail_count,

                "average_percentage":
                    aggregate[
                        "average_percentage"
                    ],

                "highest_percentage":
                    aggregate[
                        "highest_percentage"
                    ],

                "lowest_percentage":
                    aggregate[
                        "lowest_percentage"
                    ],
            }
        )