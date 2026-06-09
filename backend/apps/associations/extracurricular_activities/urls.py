# =============================================================================
# associations/urls/extracurricular_activity_urls.py
# =============================================================================

from django.urls import path

from apps.associations.extracurricular_activities.views import (
    ExtracurricularActivityAPIView
)

urlpatterns = [

    path(
        "",
        ExtracurricularActivityAPIView.as_view(),
        name="extracurricular-activity-list"
    ),

    path(
        "<int:pk>/",
        ExtracurricularActivityAPIView.as_view(),
        name="extracurricular-activity-detail"
    ),
]