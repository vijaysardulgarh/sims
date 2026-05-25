from django.urls import (

    path,

    include
)


urlpatterns = [

    # =====================================
    # AUTHENTICATION
    # =====================================

    path(
        "",
        include(
            "apps.accounts.authentication.urls"
        )
    ),

    # =====================================
    # USERS
    # =====================================

    path(
        "users/",
        include(
            "apps.accounts.users.urls"
        )
    ),

    # =====================================
    # ROLES
    # =====================================

    path(
        "roles/",
        include(
            "apps.accounts.roles.urls"
        )
    ),

    # =====================================
    # USER ROLES
    # =====================================

    path(
        "user-roles/",
        include(
            "apps.accounts.user_roles.urls"
        )
    ),

    # =====================================
    # PERMISSIONS
    # =====================================

    path(
        "permissions/",
        include(
            "apps.accounts.permissions.urls"
        )
    ),

    # =====================================
    # ROLE PERMISSIONS
    # =====================================

    path(
        "role-permissions/",
        include(
            "apps.accounts.role_permissions.urls"
        )
    ),

    # =====================================
    # USER PERMISSIONS
    # =====================================

    path(
        "user-permissions/",
        include(
            "apps.accounts.user_permissions.urls"
        )
    ),
]