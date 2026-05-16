from django.urls import path

from .views import (
    StaffSummaryAPIView,
)

urlpatterns = [

    path(
        "summary/",
        StaffSummaryAPIView.as_view(),
        name="staff-summary",
    ),
]