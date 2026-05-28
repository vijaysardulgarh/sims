from django.urls import path

from apps.schools.views import (

    SchoolListCreateAPIView,

    SchoolRetrieveUpdateDestroyAPIView,
)

urlpatterns = [

    path(
        "",
        SchoolListCreateAPIView.as_view(),
    ),

    path(
        "<int:pk>/",
        SchoolRetrieveUpdateDestroyAPIView.as_view(),
    ),
]