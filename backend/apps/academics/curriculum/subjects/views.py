from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.curriculum.subjects.models import (
    Subject
)

from apps.academics.curriculum.subjects.serializers import (
    SubjectSerializer
)


class SubjectViewSet(
    SchoolFilteredViewSet
):

    # ============================================
    # SERIALIZER
    # ============================================

    serializer_class = (
        SubjectSerializer
    )

    # ============================================
    # SEARCH
    # ============================================

    search_fields = [

        "name",

        "code"
    ]

    # ============================================
    # ORDERING
    # ============================================

    ordering_fields = [

        "name",

        "code"
    ]

    ordering = [

        "name"
    ]

    # ============================================
    # FILTERS
    # ============================================

    filterset_fields = [

        "is_language",

        "is_optional",

        "has_lab",
    ]

    # ============================================
    # QUERYSET
    # ============================================

    def get_queryset(self):

        return (

            Subject.objects

            .filter(
                is_deleted=False
            )

            .order_by("name")
        )