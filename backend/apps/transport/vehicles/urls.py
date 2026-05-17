from django.urls import path

from .views import (
    VehicleListCreateAPIView,
    VehicleRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "",
        VehicleListCreateAPIView.as_view(),
        name="vehicle-list-create"
    ),

    path(
        "<int:pk>/",
        VehicleRetrieveUpdateDestroyAPIView.as_view(),
        name="vehicle-detail"
    ),
]