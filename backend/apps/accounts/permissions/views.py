from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.accounts.permissions.models import (
    Permission
)

from apps.accounts.permissions.serializers import (
    PermissionSerializer
)


# =========================================
# PERMISSION LIST API
# =========================================

class PermissionListAPIView(

    generics.ListAPIView
):

    queryset = (

        Permission.objects.filter(

            is_deleted=False,

            is_active=True
        )

        .order_by(

            "module",

            "display_order",

            "name"
        )
    )

    serializer_class = (
        PermissionSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


# =========================================
# PERMISSION DETAIL API
# =========================================

class PermissionDetailAPIView(

    generics.RetrieveAPIView
):

    queryset = (

        Permission.objects.filter(

            is_deleted=False,

            is_active=True
        )
    )

    serializer_class = (
        PermissionSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]