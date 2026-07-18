# =============================================================================
# clusters/views.py
# =============================================================================

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.clusters.models import Cluster
from apps.clusters.serializers import ClusterSerializer


# =============================================================================
# CLUSTER LIST / CREATE
# =============================================================================

class ClusterListCreateAPIView(
    generics.ListCreateAPIView
):

    permission_classes = [
        IsAuthenticated,
    ]

    serializer_class = ClusterSerializer

    queryset = (
        Cluster.objects
        .filter(
            is_deleted=False,
        )
        .order_by("name")
    )

    def perform_create(
        self,
        serializer,
    ):

        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )


# =============================================================================
# CLUSTER DETAIL / UPDATE / DELETE
# =============================================================================

class ClusterRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAuthenticated,
    ]

    serializer_class = ClusterSerializer

    queryset = (
        Cluster.objects
        .filter(
            is_deleted=False,
        )
    )

    def perform_update(
        self,
        serializer,
    ):

        serializer.save(
            updated_by=self.request.user,
        )

    def perform_destroy(
        self,
        instance,
    ):

        instance.is_deleted = True
        instance.updated_by = self.request.user
        instance.save(
            update_fields=[
                "is_deleted",
                "updated_by",
                "updated_at",
            ]
        )


# =============================================================================
# ACTIVE CLUSTERS
# =============================================================================

class ActiveClusterListAPIView(
    generics.ListAPIView
):

    permission_classes = [
        IsAuthenticated,
    ]

    serializer_class = ClusterSerializer

    queryset = (
        Cluster.objects
        .filter(
            is_active=True,
            is_deleted=False,
        )
        .order_by("name")
    )