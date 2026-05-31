from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Branch

from .serializers import (
    BranchSerializer
)


class BranchViewSet(
    ModelViewSet
):

    queryset = (
        Branch.objects
        .select_related("school")
    )

    serializer_class = (
        BranchSerializer
    )