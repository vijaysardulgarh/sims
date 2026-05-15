from django.urls import path, include


urlpatterns = [

    path(
        "dashboard/",
        include("apps.finance.reports.dashboard.urls")
    ),

    path(
        "student-fees/",
        include(
            "apps.finance.reports.student_fee_reports.urls"
        )
    ),

    path(
        "payments/",
        include(
            "apps.finance.reports.payment_reports.urls"
        )
    ),

    path(
        "analytics/",
        include(
            "apps.finance.reports.analytics.urls"
        )
    ),
]