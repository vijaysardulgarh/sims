from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.subjects import (
    Subject
)

from apps.academics.subjects.serializer import (
    SubjectSerializer
)


class SubjectViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        SubjectSerializer
    )

    search_fields = [
        "name",
        "code"
    ]

    ordering_fields = [
        "name",
        "code"
    ]

    filterset_fields = [
        "is_language",
        "is_optional",
        "has_lab",
    ]

    def get_queryset(self):

        queryset = (
            Subject.objects.all()
        )

        return (

            self.filter_queryset_by_school(
                queryset
            )
        )