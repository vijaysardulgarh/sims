# apps/finance/urls.py

from django.urls import path, include


urlpatterns = [

    path(
        "fee-structures/",
        include(
            "apps.finance.fee_structures.urls"
        )
    ),

    path(
        "student-fees/",
        include(
            "apps.finance.student_fees.urls"
        )
    ),

    path(
        "fee-payments/",
        include(
            "apps.finance.fee_payments.urls"
        )
    ),

    path(
        "reports/",
        include(
            "apps.finance.reports.urls"
        )
    ),
]