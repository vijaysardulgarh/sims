from apps.academics.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.classrooms.models import (
    Classroom
)

from apps.academics.classrooms.serializers import (
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

        return self.filter_queryset_by_school(
            queryset
        )