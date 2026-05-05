from django.urls import path
from .views import *

urlpatterns = [

    path("attendance/", TeacherAttendanceAPIView.as_view()),
    path("attendance/<int:pk>/", TeacherAttendanceUpdateAPIView.as_view()),
    path("attendance/<int:pk>/delete/", TeacherAttendanceDeleteAPIView.as_view()),

    path("role/<str:role>/", StaffByRoleAPIView.as_view()),
    path("class-incharge/", ClassInchargeReportAPIView.as_view()),
    path("summary/", StaffSummaryAPIView.as_view()),

    path("static/", StaffStaticAPIView.as_view()),
]