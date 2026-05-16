from django.urls import path

from .views import (
    PostTypeListAPIView,
)

urlpatterns = [

    path(
        "",
        PostTypeListAPIView.as_view(),
        name="post-type-list",
    ),
]