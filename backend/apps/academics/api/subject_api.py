from rest_framework import viewsets
from rest_framework import filters

from apps.academics.models import (
    Subject,
    ClassSubject
)

from apps.academics.serializers.subject_serializers import (
    SubjectSerializer,
    ClassSubjectSerializer
)


# =========================================
# SUBJECT API
# =========================================

class SubjectViewSet(viewsets.ModelViewSet):

    queryset = Subject.objects.all()

    serializer_class = SubjectSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "name"
    ]


# =========================================
# CLASS SUBJECT API
# =========================================

class ClassSubjectViewSet(viewsets.ModelViewSet):

    queryset = (
        ClassSubject.objects.select_related(
            "class_obj",
            "stream",
            "subject"
        )
    )

    serializer_class = ClassSubjectSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "class_obj__name",
        "stream__name",
        "subject__name",
    ]