from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Library

from .serializers import (
    LibrarySerializer
)


class LibraryViewSet(
    ModelViewSet
):

    queryset = (

        Library.objects
        .select_related(
            "school",
            "room",
            "librarian"
        )
    )

    serializer_class = (
        LibrarySerializer
    )