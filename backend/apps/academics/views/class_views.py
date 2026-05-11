from rest_framework import viewsets

from apps.academics.models import (
    Class,
    Stream,
    Medium,
    Classroom,
    Section,
)

from apps.academics.serializers.class_serializers import (
    ClassSerializer,
    StreamSerializer,
    MediumSerializer,
    ClassroomSerializer,
    SectionSerializer,
)

# =========================================
# CLASS API VIEWSET
# =========================================

class ClassViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Class.objects.all()
    )

    serializer_class = (
        ClassSerializer
    )


# =========================================
# STREAM API VIEWSET
# =========================================

class StreamViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Stream.objects.all()
    )

    serializer_class = (
        StreamSerializer
    )


# =========================================
# MEDIUM API VIEWSET
# =========================================

class MediumViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Medium.objects.all()
    )

    serializer_class = (
        MediumSerializer
    )


# =========================================
# CLASSROOM API VIEWSET
# =========================================

class ClassroomViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Classroom.objects.all()
    )

    serializer_class = (
        ClassroomSerializer
    )


# =========================================
# SECTION API VIEWSET
# =========================================

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