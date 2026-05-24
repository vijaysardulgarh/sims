from django.urls import (
    path
)

from apps.schools.branches.views import (

    BranchListCreateAPIView,

    BranchDetailAPIView
)


urlpatterns = [

    # =====================================
    # BRANCH LIST / CREATE
    # =====================================

    path(
        "",
        BranchListCreateAPIView.as_view(),
        name="branch-list-create"
    ),

    # =====================================
    # BRANCH DETAIL
    # =====================================

    path(
        "<int:pk>/",
        BranchDetailAPIView.as_view(),
        name="branch-detail"
    ),
]