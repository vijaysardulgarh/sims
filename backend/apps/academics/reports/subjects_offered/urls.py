from django.urls import (
    path
)

from apps.academics.reports.subjects_offered.views import (
    SubjectsOfferedAPIView
)

urlpatterns = [

    path(
        "",
        SubjectsOfferedAPIView.as_view(),
        name="subjects-offered-report"
    ),
]