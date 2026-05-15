from apps.library.common.base_api import (
    SchoolFilteredViewSet
)

from apps.library.issues.models import (
    BookIssue
)

from apps.library.issues.serializers import (
    BookIssueSerializer
)


class BookIssueViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        BookIssueSerializer
    )

    search_fields = [

        "accession__accession_number",

        "member__user__first_name",

        "member__user__last_name",
    ]

    ordering_fields = [

        "issue_date",

        "due_date",

        "created_at",
    ]

    filterset_fields = [

        "status",

        "issue_date",

        "due_date",
    ]

    def get_queryset(self):

        queryset = (

            BookIssue.objects

            .select_related(

                "school",

                "accession",

                "accession__book",

                "member",

                "issued_by",

                "returned_by",
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

            issued_by=(
                self.request.user
            )
        )