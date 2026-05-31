from rest_framework.viewsets import ModelViewSet

from apps.schools.schools.models import School

from apps.schools.schools.serializers import (
    SchoolSerializer
)


class SchoolViewSet(
    ModelViewSet
):

    serializer_class = SchoolSerializer

    queryset = (
        School.objects.all()
    )