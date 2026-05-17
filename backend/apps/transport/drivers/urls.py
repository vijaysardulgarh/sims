from django.urls import path

from .views import (
    DriverListCreateAPIView,
    DriverRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "",
        DriverListCreateAPIView.as_view(),
        name="driver-list-create"
    ),

    path(
        "<int:pk>/",
        DriverRetrieveUpdateDestroyAPIView.as_view(),
        name="driver-detail"
    ),
]