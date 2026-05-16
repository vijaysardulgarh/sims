from django.urls import path

from .views import (
    SubjectsOfferedAPIView
)

urlpatterns = [

    path(
        "",
        SubjectsOfferedAPIView.as_view(),
        name="subjects-offered"
    ),
]