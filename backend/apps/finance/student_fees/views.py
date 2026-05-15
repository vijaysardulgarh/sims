from apps.finance.common.base_api import (
    SchoolFilteredViewSet
)

from apps.finance.student_fees.models import (
    StudentFee
)

from apps.finance.student_fees.serializers import (
    StudentFeeSerializer
)


class StudentFeeViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        StudentFeeSerializer
    )

    search_fields = [

        "student__first_name",

        "student__last_name",

        "session",
    ]

    ordering_fields = [

        "session",

        "total_amount",

        "paid_amount",

        "due_amount",

        "created_at",
    ]

    filterset_fields = [

        "session",

        "is_closed",

        "fee_structure",
    ]

    def get_queryset(self):

        queryset = (

            StudentFee.objects

            .select_related(

                "school",

                "student",

                "fee_structure",

                "fee_structure__class_obj",

                "fee_structure__stream",
            )
        )

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            school=(
                self.request.user.school
            )
        )