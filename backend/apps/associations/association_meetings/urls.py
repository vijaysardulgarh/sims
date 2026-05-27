# =============================================================================
# associations/urls/association_meeting_urls.py
# =============================================================================

from django.urls import path

from apps.associations.association_meetings.views import (
    AssociationMeetingAPIView
)

urlpatterns = [

    path(

        "",

        AssociationMeetingAPIView.as_view(),

        name="association-meeting-list"
    ),
]