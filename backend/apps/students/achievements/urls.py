from django.urls import path

from apps.students.achievements.views import (

    AchievementListAPIView,

    AchievementDetailAPIView,
)


urlpatterns = [

    # =====================================
    # ACHIEVEMENT LIST
    # =====================================

    path(

        "",

        AchievementListAPIView.as_view(),

        name="achievement-list",
    ),

    # =====================================
    # ACHIEVEMENT DETAIL
    # =====================================

    path(

        "<int:pk>/",

        AchievementDetailAPIView.as_view(),

        name="achievement-detail",
    ),
]