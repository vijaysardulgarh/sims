from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    FAQViewSet
)

router = DefaultRouter()

router.register(
    "",
    FAQViewSet,
    basename="faqs"
)

urlpatterns = router.urls