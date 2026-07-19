from django.urls import path

from .views import (
    TeacherAttendanceAPIView,
)

urlpatterns = [

    path(
        "",
        TeacherAttendanceAPIView.as_view(),
        name="teacher-attendance",
    ),

]