from rest_framework import viewsets

from apps.academics.classrooms import (
    Classroom
)

from apps.academics.classrooms.serializer import (
    ClassroomSerializer
)


class ClassroomViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Classroom.objects.all()
    )

    serializer_class = (
        ClassroomSerializer
    )