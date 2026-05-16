from django.urls import (
    path
)

from apps.academics.reports.teacher_workload.views import (
    TeacherWorkloadAPIView
)

urlpatterns = [

    path(
        "",
        TeacherWorkloadAPIView.as_view(),
        name="teacher-workload-report"
    ),
]