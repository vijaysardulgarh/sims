# =============================================================================
# association_roles/urls.py
# =============================================================================

from django.urls import path

from apps.associations.association_roles.views import (

    AssociationRoleListAPIView,
    AssociationRoleDetailAPIView,
)

urlpatterns = [

    path(

        "",

        AssociationRoleListAPIView.as_view(),

        name="association-role-list"
    ),

    path(

        "<int:pk>/",

        AssociationRoleDetailAPIView.as_view(),

        name="association-role-detail"
    ),
]