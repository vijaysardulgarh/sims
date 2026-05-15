from rest_framework.routers import (
    DefaultRouter
)

from apps.finance.student_fees.views import (
    StudentFeeViewSet
)

router = DefaultRouter()

router.register(
    r"",
    StudentFeeViewSet,
    basename="student-fee"
)

urlpatterns = router.urls