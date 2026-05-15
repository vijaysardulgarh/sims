from apps.library.common.base_api import (
    SchoolFilteredViewSet
)

from apps.library.book_accessions.models import (
    BookAccession
)

from apps.library.book_accessions.serializers import (
    BookAccessionSerializer
)


class BookAccessionViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        BookAccessionSerializer
    )

    search_fields = [

        "accession_number",

        "barcode",

        "book__title",

        "vendor",
    ]

    ordering_fields = [

        "created_at",

        "purchase_date",

        "price",
    ]

    filterset_fields = [

        "status",

        "condition",

        "book",
    ]

    def get_queryset(self):

        queryset = (

            BookAccession.objects

            .select_related(

                "school",

                "book",
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