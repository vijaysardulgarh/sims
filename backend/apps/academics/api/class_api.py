from rest_framework import viewsets
from rest_framework import filters

from django_filters.rest_framework import (
    DjangoFilterBackend
)

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
# BASE SCHOOL FILTER MIXIN
# =========================================

class SchoolFilteredViewSet(
    viewsets.ModelViewSet
):

    # =====================================
    # TEMP DEVELOPMENT MODE
    # =====================================

    permission_classes = []

    filter_backends = [

        DjangoFilterBackend,

        filters.SearchFilter,

        filters.OrderingFilter,
    ]

    # =====================================
    # GET SCHOOL
    # =====================================

    def get_school(self):

        return getattr(
            self.request.user,
            "school",
            None
        )

    # =====================================
    # FILTER BY SCHOOL
    # =====================================

    def filter_queryset_by_school(
        self,
        queryset
    ):

        school = self.get_school()

        # =================================
        # FILTER BY SCHOOL
        # =================================

        if school:

            return queryset.filter(
                school=school
            )

        # =================================
        # DEVELOPMENT FALLBACK
        # =================================

        return queryset


# =========================================
# CLASS API
# =========================================

class ClassViewSet(
    SchoolFilteredViewSet
):

    serializer_class = ClassSerializer

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "name",
        "class_order"
    ]

    filterset_fields = [
        "class_order"
    ]

    def get_queryset(self):

        queryset = Class.objects.all()

        return self.filter_queryset_by_school(
            queryset
        )


# =========================================
# STREAM API
# =========================================

class StreamViewSet(
    SchoolFilteredViewSet
):

    serializer_class = StreamSerializer

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "name"
    ]

    def get_queryset(self):

        queryset = Stream.objects.all()

        return self.filter_queryset_by_school(
            queryset
        )


# =========================================
# MEDIUM API
# =========================================

class MediumViewSet(
    SchoolFilteredViewSet
):

    serializer_class = MediumSerializer

    search_fields = [
        "name"
    ]

    ordering_fields = [
        "name"
    ]

    def get_queryset(self):

        queryset = Medium.objects.all()

        return self.filter_queryset_by_school(
            queryset
        )


# =========================================
# CLASSROOM API
# =========================================

class ClassroomViewSet(
    SchoolFilteredViewSet
):

    serializer_class = ClassroomSerializer

    search_fields = [
        "name",
        "floor"
    ]

    ordering_fields = [
        "name",
        "capacity",
        "floor"
    ]

    filterset_fields = [
        "floor"
    ]

    def get_queryset(self):

        queryset = Classroom.objects.all()

        return self.filter_queryset_by_school(
            queryset
        )


# =========================================
# SECTION API
# =========================================

class SectionViewSet(
    SchoolFilteredViewSet
):

    serializer_class = SectionSerializer

    search_fields = [

        "name",

        "class_obj__name",

        "stream__name",

        "medium__name",
    ]

    ordering_fields = [

        "name",

        "class_obj__class_order"
    ]

    filterset_fields = [

        "class_obj",

        "stream",

        "medium",

        "sub_stream"
    ]

    def get_queryset(self):

        queryset = Section.objects.select_related(

            "class_obj",

            "stream",

            "medium",

            "classroom"
        )

        return self.filter_queryset_by_school(
            queryset
        )