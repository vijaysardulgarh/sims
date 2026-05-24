from django.urls import (
    path
)

from apps.accounts.user_roles.views import (

    UserRoleListCreateAPIView,

    UserRoleDetailAPIView
)


urlpatterns = [

    # =====================================
    # USER ROLE LIST / CREATE
    # =====================================

    path(
        "",
        UserRoleListCreateAPIView.as_view(),
        name="user-role-list-create"
    ),

    # =====================================
    # USER ROLE DETAIL
    # =====================================

    path(
        "<int:pk>/",
        UserRoleDetailAPIView.as_view(),
        name="user-role-detail"
    ),
]