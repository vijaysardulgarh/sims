from apps.academics.common.base_api import (
    SchoolFilteredViewSet
)

from apps.academics.classrooms import (
    Classroom
)

from apps.academics.classrooms.serializer import (
    ClassroomSerializer
)


class ClassroomViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        ClassroomSerializer
    )

    search_fields = [
        "name",
        "floor"
    ]

    ordering_fields = [
        "name",
        "capacity",
        "floor"
    ]

    filterset_fields = [
        "floor"
    ]

    def get_queryset(self):

        queryset = (
            Classroom.objects.all()
        )

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )