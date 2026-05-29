# =============================================================================
# association_members/urls.py
# =============================================================================

from django.urls import path

from apps.associations.association_members.views import (
    AssociationMemberAPIView,
    AssociationMemberDetailAPIView,
)

urlpatterns = [

    path(
        "",
        AssociationMemberAPIView.as_view(),
        name="association-member-list"
    ),

    path(
        "<int:pk>/",
        AssociationMemberDetailAPIView.as_view(),
        name="association-member-detail"
    ),
]