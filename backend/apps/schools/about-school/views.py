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

    serializer_class = (
        AboutSchoolSerializer
    )

    def get_queryset(self):

        return (
            AboutSchool.objects
            .select_related("school")
            .order_by("school__name")
        )