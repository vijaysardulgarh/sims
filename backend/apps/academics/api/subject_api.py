from rest_framework import viewsets
from rest_framework import filters

from rest_framework.permissions import (
    IsAuthenticated
)

from django_filters.rest_framework import (
    DjangoFilterBackend
)

from apps.academics.models import (
    Subject,
    ClassSubject
)

from apps.academics.serializers.subject_serializers import (
    SubjectSerializer,
    ClassSubjectSerializer
)


# =========================================
# BASE SCHOOL FILTER VIEWSET
# =========================================

class SchoolFilteredViewSet(
    viewsets.ModelViewSet
):

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [

        DjangoFilterBackend,

        filters.SearchFilter,

        filters.OrderingFilter,
    ]

    def get_school(self):

        return getattr(
            self.request.user,
            "school",
            None
        )

    def filter_queryset_by_school(
        self,
        queryset
    ):

        school = self.get_school()

        if school:

            return queryset.filter(
                school=school
            )

        return queryset.none()


# =========================================
# SUBJECT API
# =========================================

class SubjectViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        SubjectSerializer
    )

    search_fields = [
        "name",
        "code"
    ]

    ordering_fields = [
        "name",
        "code"
    ]

    filterset_fields = [
        "is_language",
        "is_optional",
        "has_lab",
    ]

    def get_queryset(self):

        queryset = (
            Subject.objects.all()
        )

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )


# =========================================
# CLASS SUBJECT API
# =========================================

class ClassSubjectViewSet(
    SchoolFilteredViewSet
):

    serializer_class = (
        ClassSubjectSerializer
    )

    search_fields = [

        "class_obj__name",

        "stream__name",

        "subject__name",

        "sub_stream",
    ]

    ordering_fields = [

        "class_obj__class_order",

        "subject__name",

        "periods_per_week",
    ]

    filterset_fields = [

        "class_obj",

        "stream",

        "subject",

        "sub_stream",

        "is_optional",

        "has_lab",

        "is_shared",
    ]

    def get_queryset(self):

        queryset = (

            ClassSubject.objects

            .select_related(

                "school",

                "class_obj",

                "stream",

                "subject"
            )
        )

        return (

            self.filter_queryset_by_school(
                queryset
            )
        )