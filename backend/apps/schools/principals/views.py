from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Principal
from .serializers import PrincipalSerializer


class PrincipalViewSet(ModelViewSet):

    serializer_class = PrincipalSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    queryset = (
        Principal.objects
        .select_related("school")
        .order_by(
            "display_order",
            "name",
        )
    )

    def perform_create(self, serializer):

        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):

        serializer.save(
            updated_by=self.request.user,
        )