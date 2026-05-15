from apps.finance.common.base_api import (
    SchoolFilteredViewSet
)

from apps.finance.fee_payments.models import (
    FeePayment
)

from apps.finance.fee_payments.serializers import (
    FeePaymentSerializer
)


class FeePaymentViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        FeePaymentSerializer
    )

    search_fields = [

        "receipt_number",

        "transaction_id",

        "student_fee__student__first_name",

        "student_fee__student__last_name",
    ]

    ordering_fields = [

        "payment_date",

        "amount",

        "created_at",
    ]

    filterset_fields = [

        "payment_mode",

        "payment_status",

        "payment_date",
    ]

    def get_queryset(self):

        queryset = (

            FeePayment.objects

            .select_related(

                "school",

                "student_fee",

                "created_by",
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
            ),

            created_by=(
                self.request.user
            )
        )