from django.urls import path

from .views import (
    TodayCollectionView,
    PaymentModeSummaryView,
)


urlpatterns = [

    path(
        "today-collection/",
        TodayCollectionView.as_view(),
        name="today-collection-report"
    ),

    path(
        "payment-modes/",
        PaymentModeSummaryView.as_view(),
        name="payment-mode-report"
    ),
]