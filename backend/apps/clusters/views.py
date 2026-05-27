# =============================================================================
# clusters/views.py
# =============================================================================

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.clusters.models import Cluster

from apps.clusters.serializers import (
    ClusterSerializer
)

from apps.core.common.views import (

    BaseAPIView,

    BaseListCreateAPIView,

    BaseRetrieveUpdateDestroyAPIView
)


# =============================================================================
# CLUSTER LIST CREATE
# =============================================================================

class ClusterListCreateAPIView(
    BaseListCreateAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    queryset = (

        Cluster.objects.filter(
            is_deleted=False
        )
    )

    serializer_class = (
        ClusterSerializer
    )

    search_fields = [

        "name",

        "code",

        "email",

        "phone",
    ]

    ordering_fields = [

        "name",

        "code",

        "created_at",
    ]

    ordering = [
        "name"
    ]


# =============================================================================
# CLUSTER DETAIL
# =============================================================================

class ClusterRetrieveUpdateDestroyAPIView(
    BaseRetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    queryset = (

        Cluster.objects.filter(
            is_deleted=False
        )
    )

    serializer_class = (
        ClusterSerializer
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
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        queryset = (

            Cluster.objects.filter(

                is_active=True,

                is_deleted=False
            )

            .order_by("name")
        )

        serializer = (
            ClusterSerializer(

                queryset,

                many=True,

                context={
                    "request": request
                }
            )
        )

        return self.success_response(
            data=serializer.data
        )