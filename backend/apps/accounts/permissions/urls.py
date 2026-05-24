from django.urls import (
    path
)

from apps.accounts.permissions.views import (

    PermissionListAPIView,

    PermissionDetailAPIView
)


urlpatterns = [

    # =====================================
    # PERMISSION LIST
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
]