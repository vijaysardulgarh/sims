# =============================================================================
# roles/urls/role_urls.py
# =============================================================================

from django.urls import path

from apps.associations.roles.views import (

    RoleListAPIView,
    RoleDetailAPIView,
)

urlpatterns = [

    path(

        "",

        RoleListAPIView.as_view(),

        name="role-list"
    ),

    path(

        "<int:pk>/",

        RoleDetailAPIView.as_view(),

        name="role-detail"
    ),
]