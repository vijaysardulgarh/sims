from django.urls import path

from .views import (
    TeacherAssignmentAPIView
)

urlpatterns = [

    path(
        "",
        TeacherAssignmentAPIView.as_view(),
        name="teacher-subject-assignments"
    ),
]