from django.urls import (
    path
)

from .views import (
    ExamReportAPIView
)

urlpatterns = [

    path(
        "",
        ExamReportAPIView.as_view(),
        name="exam-report",
    ),
]