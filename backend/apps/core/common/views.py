from django.utils import timezone

from rest_framework import (
    filters,
    viewsets,
)

from rest_framework.views import (
    APIView
)

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.exceptions import (
    PermissionDenied
)

from django_filters.rest_framework import (
    DjangoFilterBackend
)

from apps.core.responses.success import (
    success_response
)

from apps.core.responses.error import (
    error_response
)


# =========================================
# BASE SCHOOL FILTER VIEWSET
# =========================================

class SchoolFilteredViewSet(
    viewsets.ModelViewSet
):

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [

        DjangoFilterBackend,

        filters.SearchFilter,

        filters.OrderingFilter,
    ]

    # =====================================
    # GET SCHOOL
    # =====================================

    def get_school(self):

        return getattr(
            self.request,
            "school",
            None
        )

    # =====================================
    # FILTER QUERYSET
    # =====================================

    def filter_queryset_by_school(
        self,
        queryset
    ):

        user = self.request.user

        if user.is_superuser:

            return queryset.filter(
                is_deleted=False
            )

        school = self.get_school()

        if not school:

            return queryset.none()

        return queryset.filter(

            school=school,

            is_deleted=False
        )

    # =====================================
    # GET QUERYSET
    # =====================================

    def get_queryset(self):

        queryset = super().get_queryset()

        return (
            self.filter_queryset_by_school(
                queryset
            )
        )

    # =====================================
    # OBJECT LEVEL SECURITY
    # =====================================

    def get_object(self):

        obj = super().get_object()

        if self.request.user.is_superuser:

            return obj

        if (

            hasattr(
                obj,
                "school"
            )

            and

            obj.school
            !=
            self.get_school()

        ):

            raise PermissionDenied(
                "Access denied."
            )

        return obj

    # =====================================
    # CREATE OBJECT
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        user = self.request.user

        if user.is_superuser:

            serializer.save(

                created_by=user,

                updated_by=user,
            )

            return

        serializer.save(

            school=self.get_school(),

            created_by=user,

            updated_by=user,
        )

    # =====================================
    # UPDATE OBJECT
    # =====================================

    def perform_update(
        self,
        serializer
    ):

        user = self.request.user

        if user.is_superuser:

            serializer.save(

                updated_by=user
            )

            return

        serializer.save(

            school=self.get_school(),

            updated_by=user
        )

    # =====================================
    # SOFT DELETE
    # =====================================

    def perform_destroy(
        self,
        instance
    ):

        instance.is_deleted = True

        instance.deleted_at = (
            timezone.now()
        )

        instance.deleted_by = (
            self.request.user
        )

        instance.updated_by = (
            self.request.user
        )

        instance.save(
            update_fields=[
                "is_deleted",
                "deleted_at",
                "deleted_by",
                "updated_by",
                "updated_at",
            ]
        )


# =========================================
# BASE API VIEW
# =========================================

class BaseAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =====================================
    # GET SCHOOL
    # =====================================

    def get_school(
        self
    ):

        return getattr(
            self.request,
            "school",
            None
        )

    # =====================================
    # SUCCESS RESPONSE
    # =====================================

    def success_response(
        self,
        data=None,
        message="Success",
        status_code=200
    ):

        return success_response(

            data=data,

            message=message,

            status_code=status_code
        )

    # =====================================
    # ERROR RESPONSE
    # =====================================

    def error_response(
        self,
        message="Something went wrong",
        errors=None,
        status_code=400
    ):

        return error_response(

            message=message,

            errors=errors,

            status_code=status_code
        )