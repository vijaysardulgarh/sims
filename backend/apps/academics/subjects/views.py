from apps.academics.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.subjects.models import (
    Subject
)

from apps.academics.subjects.serializers import (
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

        return self.filter_queryset_by_school(
            queryset
        )