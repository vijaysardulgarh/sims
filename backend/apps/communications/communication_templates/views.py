from rest_framework import viewsets

from .models import (
    CommunicationTemplate
)

from .serializers import (
    CommunicationTemplateSerializer
)


class CommunicationTemplateViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        CommunicationTemplate.objects
        .select_related(
            'category'
        )
        .all()
    )

    serializer_class = (
        CommunicationTemplateSerializer
    )