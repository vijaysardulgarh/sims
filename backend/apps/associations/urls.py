from django.urls import path
from .views import *

urlpatterns = [
    path("smc/", SMCMemberAPIView.as_view()),
    path("nodal/", NodalStaffAPIView.as_view()),
    path("committee/<int:pk>/", CommitteeDetailAPIView.as_view()),
    path("staff-roles/", StaffAssociationRolesAPIView.as_view()),
    path("static/", StaticCommitteeAPIView.as_view()),
]