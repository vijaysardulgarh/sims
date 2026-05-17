from django.urls import path

from .views import (
    TransportAssignmentListCreateAPIView,
    TransportAssignmentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "",
        TransportAssignmentListCreateAPIView.as_view(),
        name="transport-assignment-list-create"
    ),

    path(
        "<int:pk>/",
        TransportAssignmentRetrieveUpdateDestroyAPIView.as_view(),
        name="transport-assignment-detail"
    ),
]