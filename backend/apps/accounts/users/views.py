from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.parsers import (

    MultiPartParser,

    FormParser
)

from apps.core.common.views import (
    BaseAPIView
)

from apps.accounts.users.models import (
    User
)

from apps.accounts.users.serializers import (
    UserSerializer
)


# =========================================
# USER LIST CREATE API
# =========================================

class UserListCreateAPIView(

    BaseAPIView,
    generics.ListCreateAPIView
):

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

    # =====================================
    # GET QUERYSET
    # =====================================

    def get_queryset(
        self
    ):

        return (

            User.objects.filter(

                school=self.request.school,

                is_deleted=False
            )

            .order_by("-id")
        )

    # =====================================
    # PERFORM CREATE
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        serializer.save(

            school=self.request.school,

            created_by=self.request.user
        )


# =========================================
# USER DETAIL API
# =========================================

class UserDetailAPIView(

    BaseAPIView,
    generics.RetrieveUpdateDestroyAPIView
):

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

    # =====================================
    # GET QUERYSET
    # =====================================

    def get_queryset(
        self
    ):

        return (

            User.objects.filter(

                school=self.request.school,

                is_deleted=False
            )
        )

    # =====================================
    # PERFORM UPDATE
    # =====================================

    def perform_update(
        self,
        serializer
    ):

        serializer.save(
            updated_by=self.request.user
        )

    # =====================================
    # SOFT DELETE
    # =====================================

    def perform_destroy(
        self,
        instance
    ):

        instance.is_deleted = True

        instance.updated_by = (
            self.request.user
        )

        instance.save()