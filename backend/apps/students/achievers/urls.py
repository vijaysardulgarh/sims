from django.urls import path

from apps.students.views import (

    AchieverListAPIView,

    AchieverDetailAPIView,
)


urlpatterns = [

    # =====================================
    # ACHIEVER LIST
    # =====================================

    path(

        "",

        AchieverListAPIView.as_view(),

        name="achiever-list",
    ),

    # =====================================
    # ACHIEVER DETAIL
    # =====================================

    path(

        "<int:pk>/",

        AchieverDetailAPIView.as_view(),

        name="achiever-detail",
    ),
]