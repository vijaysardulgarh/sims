from apps.core.views.base_views import (
    SchoolFilteredViewSet
)

from .models import (
    SubjectConfiguration
)

from .serializers import (
    SubjectConfigurationSerializer
)


class SubjectConfigurationViewSet(
    SchoolFilteredViewSet
):

    queryset = (
        SubjectConfiguration.objects
        .select_related(
            "exam",
            "subject",
        )
    )

    serializer_class = (
        SubjectConfigurationSerializer
    )

    search_fields = [

        "exam__name",

        "subject__name",
    ]

    ordering_fields = [

        "maximum_marks",

        "passing_marks",

        "created_at",
    ]

    ordering = [
        "subject",
    ]