from django.urls import path

from apps.exams.views import (

    ExamNotificationListCreateAPIView,

    ExamNotificationDetailAPIView,
)


urlpatterns = [

    # =====================================
    # EXAM NOTIFICATION LIST / CREATE
    # =====================================

    path(

        "",

        ExamNotificationListCreateAPIView.as_view(),

        name="exam-notification-list-create"
    ),


    # =====================================
    # EXAM NOTIFICATION DETAIL
    # =====================================

    path(

        "<int:pk>/",

        ExamNotificationDetailAPIView.as_view(),

        name="exam-notification-detail"
    ),
]