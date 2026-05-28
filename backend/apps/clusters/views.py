# =============================================================================
# clusters/views.py
# =============================================================================

from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import (
    Response
)

from apps.clusters.models import (
    Cluster
)

from apps.clusters.serializers import (
    ClusterSerializer
)


# =============================================================================
# CLUSTER LIST CREATE
# =============================================================================

class ClusterListCreateAPIView(
    generics.ListCreateAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = (
        ClusterSerializer
    )

    queryset = (

        Cluster.objects.filter(
            is_deleted=False
        )

        .order_by("name")
    )


# =============================================================================
# CLUSTER DETAIL
# =============================================================================

class ClusterRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = (
        ClusterSerializer
    )

    queryset = (

        Cluster.objects.filter(
            is_deleted=False
        )
    )

    def perform_destroy(
        self,
        instance
    ):

        instance.is_deleted = True

        instance.save()


# =============================================================================
# ACTIVE CLUSTERS
# =============================================================================

class ActiveClusterListAPIView(
    generics.ListAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = (
        ClusterSerializer
    )

    queryset = (

        Cluster.objects.filter(

            is_active=True,

            is_deleted=False
        )

        .order_by("name")
    )