from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Recognition

from .serializers import (
    RecognitionSerializer
)


class RecognitionViewSet(
    ModelViewSet
):

    queryset = (

        Recognition.objects
        .select_related(
            "school"
        )
    )

    serializer_class = (
        RecognitionSerializer
    )