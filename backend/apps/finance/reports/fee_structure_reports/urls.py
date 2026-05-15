from django.urls import path

from .views import (
    PendingFeeReportView,
    FullyPaidReportView,
)


urlpatterns = [

    path(
        "pending/",
        PendingFeeReportView.as_view(),
        name="pending-fee-report"
    ),

    path(
        "fully-paid/",
        FullyPaidReportView.as_view(),
        name="fully-paid-report"
    ),
]