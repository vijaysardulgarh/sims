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

from .models import (
    User,
    AccessControl
)

from .serializers import (

    LoginSerializer,

    UserSerializer,

    AccessControlSerializer
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


# =========================================
# PERMISSION LIST CREATE API
# =========================================

class AccessControlListCreateAPIView(
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

        permissions = AccessControl.objects.all()

        serializer = AccessControlSerializer(

            permissions,

            many=True
        )

        return Response(
            serializer.data
        )

    def post(
        self,
        request
    ):

        serializer = AccessControlSerializer(

            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )


# =========================================
# PERMISSION DETAIL API
# =========================================

from rest_framework import generics


class AccessControlListCreateAPIView(

    generics.ListCreateAPIView
):

    queryset = (
        AccessControl.objects.all()
    )

    serializer_class = (
        AccessControlSerializer
    )



class AccessControlDetailAPIView(

    generics.RetrieveUpdateDestroyAPIView
):

    queryset = (
        AccessControl.objects.all()
    )

    serializer_class = (
        AccessControlSerializer
    )