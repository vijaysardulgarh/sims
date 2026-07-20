from django.urls import path

from .views import (
    TeacherAvailabilityTeacherListView,
    TeacherAvailabilityBulkMatrixView,
    TeacherAvailabilityBulkSaveView,
)

urlpatterns = [

    path(
        "teachers/",
        TeacherAvailabilityTeacherListView.as_view(),
    ),

    path(
        "bulk-matrix/",
        TeacherAvailabilityBulkMatrixView.as_view(),
    ),

    path(
        "bulk-save/",
        TeacherAvailabilityBulkSaveView.as_view(),
    ),

]