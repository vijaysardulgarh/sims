from django.urls import path

from apps.exams.views import (

    ExamTypeListCreateAPIView,

    ExamTypeDetailAPIView,
)


urlpatterns = [

    # =====================================
    # EXAM TYPE LIST / CREATE
    # =====================================

    path(

        "",

        ExamTypeListCreateAPIView.as_view(),

        name="exam-type-list-create"
    ),


    # =====================================
    # EXAM TYPE DETAIL
    # =====================================

    path(

        "<int:pk>/",

        ExamTypeDetailAPIView.as_view(),

        name="exam-type-detail"
    ),
]