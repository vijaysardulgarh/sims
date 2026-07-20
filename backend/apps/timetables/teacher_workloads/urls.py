from django.urls import path

from .views import (
    TeacherWorkloadListView,
    TeacherWorkloadBulkSaveView,
)

urlpatterns = [
    path(
        "",
        TeacherWorkloadListView.as_view(),
        name="teacher-workload-list",
    ),
    path(
        "save/",
        TeacherWorkloadBulkSaveView.as_view(),
        name="teacher-workload-bulk-save",
    ),
]