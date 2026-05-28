# =============================================================================
# schools/views.py
# =============================================================================

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.schools.models import School
from apps.schools.serializers import SchoolSerializer


# =============================================================================
# SCHOOL LIST + CREATE
# =============================================================================

class SchoolListCreateAPIView(
    generics.ListCreateAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = SchoolSerializer

    queryset = (

        School.objects.filter(
            is_deleted=False
        )

        .select_related("cluster")

        .order_by("name")
    )


# =============================================================================
# SCHOOL DETAIL + UPDATE + DELETE
# =============================================================================

class SchoolRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = SchoolSerializer

    queryset = (

        School.objects.filter(
            is_deleted=False
        )

        .select_related("cluster")
    )

    def perform_destroy(
        self,
        instance
    ):

        instance.is_deleted = True

        instance.save()