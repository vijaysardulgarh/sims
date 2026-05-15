# apps/finance/fee_structures/urls.py

from django.urls import path

from .views import (
    FeeStructureListCreateView,
    FeeStructureDetailView,
)

urlpatterns = [

    path(
        "",
        FeeStructureListCreateView.as_view(),
        name="fee-structure-list-create"
    ),

    path(
        "<int:pk>/",
        FeeStructureDetailView.as_view(),
        name="fee-structure-detail"
    ),
]