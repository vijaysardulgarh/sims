from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Classroom

from .serializers import (
    ClassroomSerializer
)


class ClassroomViewSet(
    ModelViewSet
):

    queryset = (

        Classroom.objects
        .select_related(
            "school",
            "room"
        )
    )

    serializer_class = (
        ClassroomSerializer
    )