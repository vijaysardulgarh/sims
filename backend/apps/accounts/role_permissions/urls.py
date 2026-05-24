from django.urls import (
    path
)

from apps.accounts.role_permissions.views import (

    RolePermissionListCreateAPIView,

    RolePermissionDetailAPIView
)


urlpatterns = [

    # =====================================
    # ROLE PERMISSION LIST / CREATE
    # =====================================

    path(
        "",
        RolePermissionListCreateAPIView.as_view(),
        name="role-permission-list-create"
    ),

    # =====================================
    # ROLE PERMISSION DETAIL
    # =====================================

    path(
        "<int:pk>/",
        RolePermissionDetailAPIView.as_view(),
        name="role-permission-detail"
    ),
]