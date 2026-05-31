from rest_framework import viewsets

from .models import (
    CommunicationCategory
)

from .serializers import (
    CommunicationCategorySerializer
)


class CommunicationCategoryViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        CommunicationCategory.objects.all()
    )

    serializer_class = (
        CommunicationCategorySerializer
    )