from django.urls import (
    path
)

from apps.accounts.roles.views import (

    RoleListCreateAPIView,

    RoleDetailAPIView
)


urlpatterns = [

    # =====================================
    # ROLE LIST / CREATE
    # =====================================

    path(
        "",
        RoleListCreateAPIView.as_view(),
        name="role-list-create"
    ),

    # =====================================
    # ROLE DETAIL
    # =====================================

    path(
        "<int:pk>/",
        RoleDetailAPIView.as_view(),
        name="role-detail"
    ),
]