# =============================================================================
# associations/urls/association_urls.py
# =============================================================================

from django.urls import path

from apps.associations.associations.views import (

    AssociationListAPIView,
    CommitteeDetailAPIView,
)

urlpatterns = [

    path(

        "",

        AssociationListAPIView.as_view(),

        name="association-list"
    ),

    path(

        "committee/<int:pk>/",

        CommitteeDetailAPIView.as_view(),

        name="committee-detail"
    ),
]