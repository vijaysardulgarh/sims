from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter
from .views import SubjectRequirementViewSet

router = DefaultRouter()
router.register(r'', SubjectRequirementViewSet, basename='subject-requirement')

urlpatterns = [
    # Explicitly map the bulk action route to handle both GET and POST seamlessly
    path(
        "bulk_assign/",
        SubjectRequirementViewSet.as_view({
            "get": "bulk_assign",
            "post": "bulk_assign",
        }),
        name="subject-requirement-bulk-assign",
    ),

    # Include standard router endpoints for standard CRUD operations
    path("", include(router.urls)),
]