from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from .views import (

    LoginAPIView,

    LogoutAPIView,

    MeAPIView,

    AccessControlListCreateAPIView,

    AccessControlDetailAPIView,
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

    # =====================================
    # ACCESS CONTROLS
    # =====================================

    path(
        "permissions/",
        AccessControlListCreateAPIView.as_view(),
        name="access_controls"
    ),

    path(
        "permissions//<int:pk>/",
        AccessControlDetailAPIView.as_view(),
        name="access_control_detail"
    ),
    
]