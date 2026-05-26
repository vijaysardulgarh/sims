from django.urls import path

from .views import (
    ModuleListCreateAPIView,
    ModuleRetrieveUpdateDestroyAPIView,
)

from apps.accounts.modules.sidebar.SidebarAPIView import (
    SidebarAPIView
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

    path(
    "sidebar/",
    SidebarAPIView.as_view(),
    name="sidebar"
),
]