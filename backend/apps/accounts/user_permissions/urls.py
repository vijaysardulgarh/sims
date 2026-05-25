from django.urls import (
    path
)

from apps.accounts.user_permissions.views import (
    UserPermissionsAPIView
)


urlpatterns = [

    path(

        "",

        UserPermissionsAPIView.as_view(),

        name="user-permissions"
    ),
]