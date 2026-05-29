# =============================================================================
# associations/urls/association_meeting_urls.py
# =============================================================================

from django.urls import path

from apps.associations.association_meetings.views import (
    AssociationMeetingAPIView,
    AssociationMeetingDetailAPIView,
)

urlpatterns = [

    # =========================================================================
    # LIST + CREATE
    # =========================================================================

    path(

        "",

        AssociationMeetingAPIView.as_view(),

        name="association-meeting-list"
    ),

    # =========================================================================
    # DETAIL + UPDATE + DELETE
    # =========================================================================

    path(

        "<int:pk>/",

        AssociationMeetingDetailAPIView.as_view(),

        name="association-meeting-detail"
    ),
]