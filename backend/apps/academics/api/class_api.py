from rest_framework import viewsets
from rest_framework import filters

from apps.academics.models import (
    Class,
    Stream,
    Medium,
    Classroom,
    Section
)

from apps.academics.serializers.class_serializers import (
    ClassSerializer,
    StreamSerializer,
    MediumSerializer,
    ClassroomSerializer,
    SectionSerializer
)

# =========================================
# CLASS API
# =========================================

class ClassViewSet(viewsets.ModelViewSet):

    queryset = Class.objects.all()

    serializer_class = ClassSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "name"
    ]


# =========================================
# STREAM API
# =========================================

class StreamViewSet(viewsets.ModelViewSet):

    queryset = Stream.objects.all()

    serializer_class = StreamSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "name"
    ]


# =========================================
# MEDIUM API
# =========================================

class MediumViewSet(viewsets.ModelViewSet):

    queryset = Medium.objects.all()

    serializer_class = MediumSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "name"
    ]


# =========================================
# CLASSROOM API
# =========================================

class ClassroomViewSet(viewsets.ModelViewSet):

    queryset = Classroom.objects.all()

    serializer_class = ClassroomSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "name",
        "floor"
    ]


# =========================================
# SECTION API
# =========================================

class SectionViewSet(viewsets.ModelViewSet):

    queryset = (
        Section.objects.select_related(
            "class_obj",
            "stream",
            "medium",
            "classroom"
        )
    )

    serializer_class = SectionSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "name",
        "class_obj__name",
        "stream__name",
        "medium__name",
    ]