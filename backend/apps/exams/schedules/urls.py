from django.urls import path

from apps.exams.views import (

    ExamScheduleListCreateAPIView,

    ExamScheduleDetailAPIView,
)


urlpatterns = [

    # =====================================
    # EXAM SCHEDULE LIST / CREATE
    # =====================================

    path(

        "",

        ExamScheduleListCreateAPIView.as_view(),

        name="exam-schedule-list-create"
    ),


    # =====================================
    # EXAM SCHEDULE DETAIL
    # =====================================

    path(

        "<int:pk>/",

        ExamScheduleDetailAPIView.as_view(),

        name="exam-schedule-detail"
    ),
]