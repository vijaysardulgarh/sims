from rest_framework import viewsets

from apps.academics.sections import (
    Section
)

from apps.academics.sections.serializer import (
    SectionSerializer
)


class SectionViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Section.objects.select_related(
            "class_obj",
            "stream",
            "medium",
            "classroom"
        )
    )

    serializer_class = (
        SectionSerializer
    )