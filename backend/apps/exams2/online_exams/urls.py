from django.urls import path

from apps.exams.views import (

    OnlineExamListCreateAPIView,

    OnlineExamDetailAPIView,
)


urlpatterns = [

    # =====================================
    # ONLINE EXAM LIST / CREATE
    # =====================================

    path(

        "",

        OnlineExamListCreateAPIView.as_view(),

        name="online-exam-list-create"
    ),


    # =====================================
    # ONLINE EXAM DETAIL
    # =====================================

    path(

        "<int:pk>/",

        OnlineExamDetailAPIView.as_view(),

        name="online-exam-detail"
    ),
]