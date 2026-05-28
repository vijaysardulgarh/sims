from django.urls import path

from .views import (
    ClassInchargeReportAPIView,
)

urlpatterns = [

    path(
        "",
        ClassInchargeReportAPIView.as_view(),
        name="class-incharge-report",
    ),
]