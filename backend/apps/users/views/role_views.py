from rest_framework import status

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


from apps.users.models.role_model import (
    Role
)

from apps.users.serializers.role_serializer import (
    RoleSerializer
)


# ==========================================
# ROLE LIST CREATE API VIEW
# ==========================================

class RoleListCreateAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]


    # ======================================
    # GET ALL ROLES
    # ======================================

    def get(
        self,
        request
    ):

        roles = Role.objects.all().order_by(
            "id"
        )

        serializer = RoleSerializer(

            roles,

            many=True
        )

        return Response(

            serializer.data,

            status=status.HTTP_200_OK
        )


    # ======================================
    # CREATE ROLE
    # ======================================

    def post(
        self,
        request
    ):

        serializer = RoleSerializer(

            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(

                serializer.data,

                status=status.HTTP_201_CREATED
            )

        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST
        )


# ==========================================
# ROLE DETAIL API VIEW
# ==========================================

class RoleDetailAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]


    # ======================================
    # GET OBJECT
    # ======================================

    def get_object(
        self,
        pk
    ):

        try:

            return Role.objects.get(
                pk=pk
            )

        except Role.DoesNotExist:

            return None


    # ======================================
    # GET SINGLE ROLE
    # ======================================

    def get(
        self,
        request,
        pk
    ):

        role = self.get_object(pk)

        if not role:

            return Response(

                {
                    "detail":
                    "Role not found"
                },

                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RoleSerializer(role)

        return Response(

            serializer.data,

            status=status.HTTP_200_OK
        )


    # ======================================
    # UPDATE ROLE
    # ======================================

    def patch(
        self,
        request,
        pk
    ):

        role = self.get_object(pk)

        if not role:

            return Response(

                {
                    "detail":
                    "Role not found"
                },

                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RoleSerializer(

            role,

            data=request.data,

            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(

                serializer.data,

                status=status.HTTP_200_OK
            )

        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST
        )


    # ======================================
    # DELETE ROLE
    # ======================================

    def delete(
        self,
        request,
        pk
    ):

        role = self.get_object(pk)

        if not role:

            return Response(

                {
                    "detail":
                    "Role not found"
                },

                status=status.HTTP_404_NOT_FOUND
            )

        role.delete()

        return Response(

            {
                "detail":
                "Role deleted successfully"
            },

            status=status.HTTP_204_NO_CONTENT
        )