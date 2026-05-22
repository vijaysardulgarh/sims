from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from apps.users.views.auth_views import (

    LoginAPIView,

    LogoutAPIView,

    MeAPIView
)

from apps.users.views.access_control_views import (

    AccessControlListCreateAPIView,

    AccessControlDetailAPIView
)

from apps.users.views.role_views import (

    RoleListCreateAPIView,

    RoleDetailAPIView
)

from apps.users.views.user_views import (

    UserListCreateAPIView,

    UserDetailAPIView
)


urlpatterns = [

    # =========================================
    # AUTH
    # =========================================

    path(
        "login/",
        LoginAPIView.as_view(),
        name="login"
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    path(
        "logout/",
        LogoutAPIView.as_view(),
        name="logout"
    ),

    path(
        "me/",
        MeAPIView.as_view(),
        name="me"
    ),


    # =========================================
    # PERMISSIONS
    # =========================================

    path(
        "permissions/",
        AccessControlListCreateAPIView.as_view(),
        name="permissions"
    ),

    path(
        "permissions/<int:pk>/",
        AccessControlDetailAPIView.as_view(),
        name="permission_detail"
    ),


    # =========================================
    # ROLES
    # =========================================

    path(
        "roles/",
        RoleListCreateAPIView.as_view(),
        name="roles"
    ),

    path(
        "roles/<int:pk>/",
        RoleDetailAPIView.as_view(),
        name="role_detail"
    ),


    # =========================================
    # USERS
    # =========================================

    path(
        "",
        UserListCreateAPIView.as_view(),
        name="users"
    ),

    path(
        "<int:pk>/",
        UserDetailAPIView.as_view(),
        name="user_detail"
    ),
]