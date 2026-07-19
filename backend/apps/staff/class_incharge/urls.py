from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ClassInchargeViewSet,
    ClassInchargeReportAPIView,
)

router = DefaultRouter()

router.register(
    "",
    ClassInchargeViewSet,
    basename="class-incharge",
)

urlpatterns = [

    # CRUD API
    path(
        "",
        include(router.urls),
    ),

    # Report API
    path(
        "report/",
        ClassInchargeReportAPIView.as_view(),
        name="class-incharge-report",
    ),
]