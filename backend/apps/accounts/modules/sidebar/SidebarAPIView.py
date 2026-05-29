from django.db.models import Q

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.accounts.modules.models import (
    Module
)

from apps.accounts.user_roles.models import (
    UserRole
)

from apps.accounts.role_permissions.models import (
    RolePermission
)


# =========================================
# SIDEBAR API
# =========================================

class SidebarAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =====================================
    # GET SIDEBAR
    # =====================================

    def get(
        self,
        request
    ):

        user = request.user

        # ==================================
        # USER ROLES
        # ==================================

        user_roles = UserRole.objects.filter(

            user=user,

            is_active=True,

            is_deleted=False,
        ).select_related(
            "role"
        )

        roles = [

            user_role.role

            for user_role in user_roles
        ]

        if not roles:

            return Response([])

        # ==================================
        # ROLE PERMISSIONS
        # ==================================

        role_permissions = (

            RolePermission.objects.filter(

                role__in=roles,

                is_active=True,

                is_deleted=False,
            )

            .select_related(

                "permission",

                "permission__module"
            )
        )

        # ==================================
        # MODULE IDS
        # ==================================

        module_ids = list(

            set(

                role_permissions.values_list(

                    "permission__module_id",

                    flat=True
                )
            )
        )

        # ==================================
        # MODULES
        # ==================================

        modules = Module.objects.filter(

            is_active=True,

            is_deleted=False,

            is_menu=True,
        ).filter(

            Q(
                id__in=module_ids
            ) |

            Q(
                children__id__in=module_ids
            )
        ).distinct().order_by(

            "order",

            "name"
        )

        # ==================================
        # PARENT MODULES
        # ==================================

        parent_modules = modules.filter(
            parent__isnull=True
        )

        sidebar_data = []

        # ==================================
        # BUILD SIDEBAR TREE
        # ==================================

        for parent in parent_modules:

            children = modules.filter(
                parent_id=parent.id
            )

            sidebar_data.append({

                "id": parent.id,

                "name": parent.name,

                "slug": parent.slug,

                "path": parent.path,

                "icon": parent.icon,

                "children": [

                    {

                        "id": child.id,

                        "name": child.name,

                        "slug": child.slug,

                        "path": child.path,

                        "icon": child.icon,
                    }

                    for child in children
                ]
            })

        return Response(
            sidebar_data
        )