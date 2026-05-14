from rest_framework import viewsets
from rest_framework import filters

from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from rest_framework.permissions import (
    IsAuthenticated
)

from django_filters.rest_framework import (
    DjangoFilterBackend
)

from apps.core.utils.helpers import (
    get_current_school
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
            self.request.user,
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

        school = self.get_school()

        if school:

            return queryset.filter(
                school=school
            )

        return queryset.none()

    # =====================================
    # AUTO ASSIGN SCHOOL
    # =====================================

    def perform_create(
        self,
        serializer
    ):

        school = self.get_school()

        if school:

            serializer.save(
                school=school
            )

        else:

            serializer.save()

    # =====================================
    # AUTO ASSIGN SCHOOL UPDATE
    # =====================================

    def perform_update(
        self,
        serializer
    ):

        serializer.save()


# =========================================
# BASE REPORT API VIEW
# =========================================

class BaseReportAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =====================================
    # GET CURRENT SCHOOL
    # =====================================

    def get_school(
        self,
        request
    ):

        return get_current_school(
            request
        )

    # =====================================
    # SCHOOL ERROR RESPONSE
    # =====================================

    def school_error_response(
        self
    ):

        return Response({

            "success": False,

            "message":
                "School not selected."

        }, status=400)

    # =====================================
    # SUCCESS RESPONSE
    # =====================================

    def success_response(
        self,
        data=None,
        message="Success",
        status_code=200
    ):

        return Response({

            "success": True,

            "message": message,

            "data": data

        }, status=status_code)

    # =====================================
    # ERROR RESPONSE
    # =====================================

    def error_response(
        self,
        message="Something went wrong",
        status_code=400
    ):

        return Response({

            "success": False,

            "message": message

        }, status=status_code)


# =========================================
# BASE SIMPLE API VIEW
# =========================================

class BaseAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =====================================
    # SUCCESS RESPONSE
    # =====================================

    def success_response(
        self,
        data=None,
        message="Success",
        status_code=200
    ):

        return Response({

            "success": True,

            "message": message,

            "data": data

        }, status=status_code)

    # =====================================
    # ERROR RESPONSE
    # =====================================

    def error_response(
        self,
        message="Something went wrong",
        status_code=400
    ):

        return Response({

            "success": False,

            "message": message

        }, status=status_code)