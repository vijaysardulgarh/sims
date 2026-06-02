# =============================================================================
# meetings/urls/meeting_urls.py
# =============================================================================

from django.urls import path

from apps.associations.meetings.views import (
    MeetingAPIView,
    MeetingDetailAPIView,
)

urlpatterns = [

    # =========================================================================
    # LIST + CREATE
    # =========================================================================

    path(
        "",
        MeetingAPIView.as_view(),
        name="meeting-list"
    ),

    # =========================================================================
    # DETAIL + UPDATE + DELETE
    # =========================================================================

    path(
        "<int:pk>/",
        MeetingDetailAPIView.as_view(),
        name="meeting-detail"
    ),
]