# =============================================================================
# schools/views.py
# =============================================================================

from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework import status

from apps.schools.models import (
    School
)

from apps.schools.serializers import (
    SchoolSerializer
)


# =============================================================================
# SCHOOL LIST
# =============================================================================

class SchoolListAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        queryset = (

            School.objects.filter(

                is_active=True,

                is_deleted=False
            )

            .select_related(
                "cluster"
            )

            .order_by("name")
        )

        serializer = (
            SchoolSerializer(

                queryset,

                many=True,

                context={
                    "request": request
                }
            )
        )

        return Response({

            "success": True,

            "count": queryset.count(),

            "results": serializer.data
        })


# =============================================================================
# SELECT SCHOOL
# =============================================================================

class SelectSchoolAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request
    ):

        school_id = request.data.get(
            "school_id"
        )

        if not school_id:

            return Response(

                {
                    "success": False,

                    "message":
                        "School ID required"
                },

                status=(
                    status.HTTP_400_BAD_REQUEST
                )
            )

        school = (

            School.objects.filter(

                id=school_id,

                is_active=True,

                is_deleted=False
            )

            .first()
        )

        if not school:

            return Response(

                {
                    "success": False,

                    "message":
                        "School not found"
                },

                status=(
                    status.HTTP_404_NOT_FOUND
                )
            )

        request.session["school_id"] = (
            school.id
        )

        return Response({

            "success": True,

            "message":
                "School selected",

            "school": {

                "id":
                    school.id,

                "name":
                    school.name,

                "slug":
                    school.slug,
            }
        })


# =============================================================================
# CLEAR SCHOOL
# =============================================================================

class ClearSchoolAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request
    ):

        request.session.pop(
            "school_id",
            None
        )

        return Response({

            "success": True,

            "message":
                "School cleared"
        })


# =============================================================================
# CURRENT SCHOOL
# =============================================================================

class CurrentSchoolAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school_id = request.session.get(
            "school_id"
        )

        if not school_id:

            return Response({

                "success": True,

                "selected_school": None
            })

        school = (

            School.objects.filter(

                id=school_id,

                is_active=True,

                is_deleted=False
            )

            .select_related(
                "cluster"
            )

            .first()
        )

        if not school:

            return Response({

                "success": True,

                "selected_school": None
            })

        serializer = (
            SchoolSerializer(

                school,

                context={
                    "request": request
                }
            )
        )

        return Response({

            "success": True,

            "selected_school":
                serializer.data
        })