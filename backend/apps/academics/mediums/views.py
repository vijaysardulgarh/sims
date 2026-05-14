from rest_framework import viewsets

from apps.academics.mediums import (
    Medium
)

from apps.academics.mediums.serializer import (
    MediumSerializer
)


class MediumViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Medium.objects.all()
    )

    serializer_class = (
        MediumSerializer
    )