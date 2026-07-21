from django.urls import path

from .views import (
    TeacherAvailabilityTeacherListView,
    TeacherAvailabilityBulkMatrixView,
    TeacherAvailabilityBulkSaveView,
)

app_name = "teacher_availability" # Optional: sets a namespace for this app

urlpatterns = [
    path(
        "teachers/",
        TeacherAvailabilityTeacherListView.as_view(),
        name="teacher-list"
    ),
    path(
        "bulk-matrix/",
        TeacherAvailabilityBulkMatrixView.as_view(),
        name="bulk-matrix"
    ),
    path(
        "bulk-save/",
        TeacherAvailabilityBulkSaveView.as_view(),
        name="bulk-save"
    ),
]