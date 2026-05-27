# =============================================================================
# clusters/urls.py
# =============================================================================

from django.urls import path

from apps.clusters.views import (

    ClusterListCreateAPIView,

    ClusterRetrieveUpdateDestroyAPIView,

    ActiveClusterListAPIView
)

urlpatterns = [

    # =====================================
    # CLUSTER LIST CREATE
    # =====================================

    path(

        "",

        ClusterListCreateAPIView.as_view(),

        name="cluster-list-create"
    ),

    # =====================================
    # ACTIVE CLUSTERS
    # =====================================

    path(

        "active/",

        ActiveClusterListAPIView.as_view(),

        name="active-cluster-list"
    ),

    # =====================================
    # CLUSTER DETAIL
    # =====================================

    path(

        "<int:pk>/",

        ClusterRetrieveUpdateDestroyAPIView.as_view(),

        name="cluster-detail"
    ),
]