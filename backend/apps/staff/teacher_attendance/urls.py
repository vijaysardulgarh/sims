from django.urls import path

from .views import (
    TeacherAttendanceAPIView,
    TeacherAttendanceUpdateAPIView,
    TeacherAttendanceDeleteAPIView,
)

urlpatterns = [

    path(
        "",
        TeacherAttendanceAPIView.as_view(),
        name="teacher-attendance",
    ),

    path(
        "<int:pk>/update/",
        TeacherAttendanceUpdateAPIView.as_view(),
        name="teacher-attendance-update",
    ),

    path(
        "<int:pk>/delete/",
        TeacherAttendanceDeleteAPIView.as_view(),
        name="teacher-attendance-delete",
    ),
]