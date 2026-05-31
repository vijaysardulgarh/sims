from rest_framework.viewsets import (
    ModelViewSet
)

from .models import AboutSchool

from .serializers import (
    AboutSchoolSerializer
)


class AboutSchoolViewSet(
    ModelViewSet
):

    queryset = (
        AboutSchool.objects
        .select_related("school")
    )

    serializer_class = (
        AboutSchoolSerializer
    )