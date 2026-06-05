from django.urls import path

from .views import (
    RollCallAPIView,
    RollCallLinkAPIView,
)

from .views.roll_call_excel import (
    RollCallExcelAPIView,
)

urlpatterns = [

    path(
        "links/",
        RollCallLinkAPIView.as_view(),
        name="roll-call-links",
    ),

    path(
        "excel/",
        RollCallExcelAPIView.as_view(),
        name="roll-call-excel",
    ),

    path(
        "",
        RollCallAPIView.as_view(),
        name="roll-call",
    ),

]