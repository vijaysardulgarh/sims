from rest_framework import viewsets

from apps.academics.classes import (
    Class
)

from apps.academics.classes.serializer import (
    ClassSerializer
)


class ClassViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Class.objects.all()
    )

    serializer_class = (
        ClassSerializer
    )