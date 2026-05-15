# apps/finance/reports/analytics/urls.py

from django.urls import path

from .views import (
    MonthlyCollectionChartView,
)

urlpatterns = [

    path(
        "monthly-collection/",
        MonthlyCollectionChartView.as_view(),
        name="monthly-collection-chart"
    ),
]