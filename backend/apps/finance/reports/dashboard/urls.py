from django.urls import path

from .views import FinanceDashboardView


urlpatterns = [
    path(
        "",
        FinanceDashboardView.as_view(),
        name="finance-dashboard-report"
    ),
]