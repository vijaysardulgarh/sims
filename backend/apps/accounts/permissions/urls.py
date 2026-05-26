from django.urls import (
    path
)

from apps.accounts.permissions.views import (

    PermissionListAPIView,

    PermissionDetailAPIView,

    PermissionByModuleAPIView,
)


urlpatterns = [

    # =====================================
    # PERMISSION LIST + CREATE
    # =====================================

    path(
        "",
        PermissionListAPIView.as_view(),
        name="permission-list"
    ),

    # =====================================
    # PERMISSION DETAIL
    # =====================================

    path(
        "<int:pk>/",
        PermissionDetailAPIView.as_view(),
        name="permission-detail"
    ),

    # =====================================
    # PERMISSIONS BY MODULE
    # =====================================

    path(
        "module/<int:module_id>/",
        PermissionByModuleAPIView.as_view(),
        name="permissions-by-module"
    ),
]