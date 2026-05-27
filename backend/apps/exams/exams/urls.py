from django.urls import path

from apps.exams.views import (

    ExamListCreateAPIView,

    ExamDetailAPIView,
)


urlpatterns = [

    # =====================================
    # EXAM LIST / CREATE
    # =====================================

    path(

        "",

        ExamListCreateAPIView.as_view(),

        name="exam-list-create"
    ),


    # =====================================
    # EXAM DETAIL
    # =====================================

    path(

        "<int:pk>/",

        ExamDetailAPIView.as_view(),

        name="exam-detail"
    ),
]