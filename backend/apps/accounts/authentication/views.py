from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (

    IsAuthenticated,

    AllowAny
)

from rest_framework import status

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from rest_framework_simplejwt.tokens import (
    RefreshToken
)

from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)

from rest_framework_simplejwt.exceptions import (
    TokenError
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.accounts.authentication.serializers import (
    LoginSerializer
)

from apps.accounts.users.serializers import (
    UserSerializer
)


# =========================================
# LOGIN API
# =========================================

class LoginAPIView(
    TokenObtainPairView
):

    permission_classes = [
        AllowAny
    ]

    serializer_class = (
        LoginSerializer
    )


# =========================================
# LOGOUT API
# =========================================

class LogoutAPIView(
    BaseAPIView,
    APIView
):

    authentication_classes = [
        JWTAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request
    ):

        refresh_token = request.data.get(
            "refresh"
        )

        if not refresh_token:

            return Response(

                {
                    "detail":
                    "Refresh token is required."
                },

                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            token = RefreshToken(
                refresh_token
            )

            token.blacklist()

            return Response(

                {
                    "message":
                    "Logged out successfully."
                },

                status=status.HTTP_200_OK
            )

        except TokenError:

            return Response(

                {
                    "detail":
                    "Invalid or expired refresh token."
                },

                status=status.HTTP_400_BAD_REQUEST
            )


# =========================================
# CURRENT USER API
# =========================================

class CurrentUserAPIView(
    BaseAPIView,
    APIView
):

    authentication_classes = [
        JWTAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        serializer = UserSerializer(

            request.user,

            context={
                "request": request
            }
        )

        return Response(

            serializer.data,

            status=status.HTTP_200_OK
        )