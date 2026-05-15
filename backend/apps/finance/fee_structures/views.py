from apps.finance.common.base_api import (
    SchoolFilteredViewSet
)

from apps.finance.fee_structures.models import (
    FeeStructure
)

from apps.finance.fee_structures.serializers import (
    FeeStructureSerializer
)


class FeeStructureViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        FeeStructureSerializer
    )

    search_fields = [

        "class_obj__name",

        "stream__name",

        "session",
    ]

    ordering_fields = [

        "session",

        "created_at",
    ]

    filterset_fields = [

        "class_obj",

        "stream",

        "session",

        "is_active",
    ]

    def get_queryset(self):

        queryset = (

            FeeStructure.objects

            .select_related(

                "school",

                "class_obj",

                "stream",
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