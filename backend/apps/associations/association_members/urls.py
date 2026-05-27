# =============================================================================
# associations/urls/association_member_urls.py
# =============================================================================

from django.urls import path

from apps.associations.association_members.views import (
    AssociationMemberAPIView
)

urlpatterns = [

    path(

        "",

        AssociationMemberAPIView.as_view(),

        name="association-member-list"
    ),
]