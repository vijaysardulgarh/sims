from django.urls import (
    path
)

from apps.accounts.users.views import (

    UserListCreateAPIView,

    UserDetailAPIView
)


urlpatterns = [

    # =====================================
    # USER LIST / CREATE
    # =====================================

    path(
        "",
        UserListCreateAPIView.as_view(),
        name="user-list-create"
    ),

    # =====================================
    # USER DETAIL
    # =====================================

    path(
        "<int:pk>/",
        UserDetailAPIView.as_view(),
        name="user-detail"
    ),
]