from rest_framework.routers import (
    DefaultRouter
)

from apps.finance.fee_payments.views import (
    FeePaymentViewSet
)

router = DefaultRouter()

router.register(
    r"",
    FeePaymentViewSet,
    basename="fee-payment"
)

urlpatterns = router.urls