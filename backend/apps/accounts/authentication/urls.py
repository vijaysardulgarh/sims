from django.urls import (
    path
)

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from apps.accounts.authentication.views import (

    LoginAPIView,

    LogoutAPIView,

    CurrentUserAPIView
)


urlpatterns = [

    # =====================================
    # LOGIN
    # =====================================

    path(
        "login/",
        LoginAPIView.as_view(),
        name="login"
    ),

    # =====================================
    # REFRESH TOKEN
    # =====================================

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh"
    ),

    # =====================================
    # LOGOUT
    # =====================================

    path(
        "logout/",
        LogoutAPIView.as_view(),
        name="logout"
    ),

    # =====================================
    # CURRENT USER
    # =====================================

    path(
        "me/",
        CurrentUserAPIView.as_view(),
        name="current-user"
    ),
]