from django.urls import path

from .views import (
    ModuleListCreateAPIView,
    ModuleRetrieveUpdateDestroyAPIView,
)


urlpatterns = [

    path(
        "",
        ModuleListCreateAPIView.as_view(),
        name="module-list-create",
    ),

    path(
        "<int:pk>/",
        ModuleRetrieveUpdateDestroyAPIView.as_view(),
        name="module-detail",
    ),
]