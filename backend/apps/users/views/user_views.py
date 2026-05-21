from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from apps.users.models.user_model import (
    User
)

from apps.users.serializers.UserSerializer import (
    UserSerializer
)


# =========================================
# USER LIST CREATE API
# =========================================

class UserListCreateAPIView(

    generics.ListCreateAPIView
):

    queryset = (
        User.objects.all()
    )

    serializer_class = (
        UserSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    parser_classes = [

        MultiPartParser,

        FormParser
    ]


# =========================================
# USER DETAIL API
# =========================================

class UserDetailAPIView(

    generics.RetrieveUpdateDestroyAPIView
):

    queryset = (
        User.objects.all()
    )

    serializer_class = (
        UserSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    parser_classes = [

        MultiPartParser,

        FormParser
    ]