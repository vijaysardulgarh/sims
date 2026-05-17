from django.urls import path

from .views import (
    TransportRouteListCreateAPIView,
    TransportRouteRetrieveUpdateDestroyAPIView,
    TransportStopListCreateAPIView,
)

urlpatterns = [
    path(
        "",
        TransportRouteListCreateAPIView.as_view(),
        name="transport-route-list-create"
    ),

    path(
        "<int:pk>/",
        TransportRouteRetrieveUpdateDestroyAPIView.as_view(),
        name="transport-route-detail"
    ),

    path(
        "stops/",
        TransportStopListCreateAPIView.as_view(),
        name="transport-stop-list-create"
    ),
]