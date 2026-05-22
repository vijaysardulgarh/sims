from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.users.models.access_control_model import (
    AccessControl
)

from apps.users.serializers.AccessControlSerializer import (
    AccessControlSerializer
)


# =========================================
# ACCESS CONTROL LIST CREATE API
# =========================================

class AccessControlListCreateAPIView(

    generics.ListCreateAPIView
):

    queryset = (
        AccessControl.objects.all()
    )

    serializer_class = (
        AccessControlSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


# =========================================
# ACCESS CONTROL DETAIL API
# =========================================

class AccessControlDetailAPIView(

    generics.RetrieveUpdateDestroyAPIView
):

    queryset = (
        AccessControl.objects.all()
    )

    serializer_class = (
        AccessControlSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]