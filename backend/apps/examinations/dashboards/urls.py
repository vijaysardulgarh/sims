from django.urls import (
    path
)

from .views import (
    ExamDashboardAPIView
)

urlpatterns = [

    path(
        "",
        ExamDashboardAPIView.as_view(),
        name="exam-dashboard",
    ),
]