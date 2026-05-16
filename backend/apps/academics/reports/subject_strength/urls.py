from django.urls import (
    path
)

from apps.academics.reports.subject_strength.views import (
    SubjectStrengthAPIView
)

urlpatterns = [

    path(
        "",
        SubjectStrengthAPIView.as_view(),
        name="subject-strength-report"
    ),
]