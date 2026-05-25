from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.accounts.users.models import (
    User
)

from apps.accounts.user_roles.models import (
    UserRole
)

from apps.accounts.role_permissions.models import (
    RolePermission
)

from apps.accounts.user_permissions.serializers import (
    UserPermissionSerializer
)


# =========================================
# USER PERMISSIONS MATRIX API
# =========================================

class UserPermissionsAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]


    # =====================================
    # GET
    # =====================================

    def get(
        self,
        request
    ):

        users = User.objects.all()

        data = []


        for user in users:

            # =================================
            # USER ROLES
            # =================================

            user_roles = (

                UserRole.objects

                .select_related(
                    "role"
                )

                .filter(

                    user=user,

                    is_deleted=False
                )
            )


            roles = [

                item.role.name

                for item in user_roles
            ]


            # =================================
            # ROLE IDS
            # =================================

            role_ids = [

                item.role.id

                for item in user_roles
            ]


            # =================================
            # ROLE PERMISSIONS
            # =================================

            role_permissions = (

                RolePermission.objects

                .select_related(
                    "permission"
                )

                .filter(

                    role_id__in=role_ids,

                    is_deleted=False
                )
            )


            permissions = list(

                set([

                    item.permission.code

                    for item in role_permissions
                ])
            )


            data.append({

                "id":
                user.id,

                "full_name":

                getattr(
                    user,
                    "full_name",
                    ""
                ),

                "email":
                user.email,

                "school":

                str(user.school)

                if getattr(

                    user,

                    "school",

                    None
                )

                else None,

                "roles":
                roles,

                "permissions":
                permissions,
            })


        serializer = (

            UserPermissionSerializer(

                data,

                many=True
            )
        )

        return Response(
            serializer.data
        )