from rest_framework import viewsets

from .models import Notification

from .serializers import (
    NotificationSerializer
)


class NotificationViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Notification.objects.select_related(
            'template'
        )
    )

    serializer_class = (
        NotificationSerializer
    )