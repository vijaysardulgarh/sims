from django.urls import path

from .views import (
    StaffByRoleAPIView,
    StaffStaticAPIView,
)

urlpatterns = [

    path(
        "role/<str:role>/",
        StaffByRoleAPIView.as_view(),
        name="staff-by-role",
    ),

    path(
        "static/",
        StaffStaticAPIView.as_view(),
        name="staff-static",
    ),
]