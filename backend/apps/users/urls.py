from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from .views import (
    LoginAPIView,
    LogoutAPIView,
    MeAPIView
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

]