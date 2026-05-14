from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.class_subjects.model import (
    ClassSubject
)

from apps.academics.class_subjects.serializer import (
    ClassSubjectSerializer
)


class ClassSubjectViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        ClassSubjectSerializer
    )

    search_fields = [

        "class_obj__name",

        "stream__name",

        "subject__name",

        "sub_stream",
    ]

    ordering_fields = [

        "class_obj__class_order",

        "subject__name",

        "periods_per_week",
    ]

    filterset_fields = [

        "class_obj",

        "stream",

        "subject",

        "sub_stream",

        "is_optional",

        "has_lab",

        "is_shared",
    ]

    def get_queryset(self):

        queryset = (

            ClassSubject.objects

            .select_related(

                "school",

                "class_obj",

                "stream",

                "subject"
            )
        )

        return (

            self.filter_queryset_by_school(
                queryset
            )
        )