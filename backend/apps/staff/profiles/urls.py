from rest_framework.routers import DefaultRouter

from apps.staff.profiles.views import StaffViewSet


router = DefaultRouter()

router.register(
    "staff-profiles",
    StaffViewSet,
    basename="staff-profiles"
)

urlpatterns = router.urls