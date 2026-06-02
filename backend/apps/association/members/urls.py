# =============================================================================
# members/urls/member_urls.py
# =============================================================================

from django.urls import path

from apps.associations.members.views import (
    MemberAPIView,
    MemberDetailAPIView,
)

urlpatterns = [

    path(
        "",
        MemberAPIView.as_view(),
        name="member-list"
    ),

    path(
        "<int:pk>/",
        MemberDetailAPIView.as_view(),
        name="member-detail"
    ),
]