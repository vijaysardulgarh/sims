from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from rest_framework_simplejwt.tokens import (
    RefreshToken
)

from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)

from apps.users.serializers.LoginSerializer import (

    LoginSerializer,

)    

from apps.users.serializers.UserSerializer import (

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

    serializer_class = LoginSerializer


# =========================================
# LOGOUT API
# =========================================

class LogoutAPIView(
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

        try:

            refresh_token = request.data.get(
                "refresh"
            )

            token = RefreshToken(
                refresh_token
            )

            token.blacklist()

            return Response({

                "message":
                    "Logged out successfully"
            })

        except Exception:

            return Response({

                "error":
                    "Invalid refresh token"

            }, status=400)


# =========================================
# CURRENT USER API
# =========================================

class MeAPIView(
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
            request.user
        )

        return Response(
            serializer.data
        )