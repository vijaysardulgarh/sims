from apps.library.common.base_api import (
    SchoolFilteredViewSet
)

from apps.library.categories.models import (
    BookCategory
)

from apps.library.categories.serializers import (
    BookCategorySerializer
)


class BookCategoryViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        BookCategorySerializer
    )

    search_fields = [

        "name",

        "code",
    ]

    ordering_fields = [

        "name",

        "created_at",
    ]

    filterset_fields = [

        "is_active",
    ]

    def get_queryset(self):

        queryset = (
            BookCategory.objects.all()
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