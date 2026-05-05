from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


# =========================================
# LOGIN API (FULL CONVERSION)
# =========================================
class LoginAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password required"},
                status=400
            )

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status=401
            )

        # OPTIONAL: session login (if you want)
        login(request, user)

        # Token for React
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Login successful",
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        })


# =========================================
# LOGOUT API
# =========================================
class LogoutAPIView(APIView):

    def post(self, request):

        # delete token if exists
        if request.user.is_authenticated:
            Token.objects.filter(user=request.user).delete()

        logout(request)

        return Response({"message": "Logged out successfully"})


# =========================================
# CHECK AUTH (FOR REACT)
# =========================================
class MeAPIView(APIView):

    def get(self, request):

        if not request.user.is_authenticated:
            return Response({"error": "Not authenticated"}, status=401)

        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        })