from rest_framework.viewsets import (
    ModelViewSet
)

from .models import (
    MandatoryPublicDisclosure
)

from .serializers import (
    MandatoryPublicDisclosureSerializer
)


class MandatoryPublicDisclosureViewSet(
    ModelViewSet
):

    queryset = (

        MandatoryPublicDisclosure
        .objects
        .select_related(
            "school"
        )
    )

    serializer_class = (
        MandatoryPublicDisclosureSerializer
    )