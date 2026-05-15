from apps.library.common.base_api import (
    SchoolFilteredViewSet
)

from apps.library.books.models import (
    Book
)

from apps.library.books.serializers import (
    BookSerializer
)


class BookViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        BookSerializer
    )

    search_fields = [

        "title",

        "author",

        "isbn",

        "publisher",
    ]

    ordering_fields = [

        "title",

        "author",

        "created_at",
    ]

    filterset_fields = [

        "category",

        "status",

        "language",
    ]

    def get_queryset(self):

        queryset = (
            Book.objects.all()
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