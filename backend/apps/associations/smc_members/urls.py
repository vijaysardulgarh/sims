# =============================================================================
# associations/urls/smc_member_urls.py
# =============================================================================

from django.urls import path

from apps.associations.smc_members.views import (
    SMCMemberAPIView
)

urlpatterns = [

    path(

        "",

        SMCMemberAPIView.as_view(),

        name="smc-member-list"
    ),
]