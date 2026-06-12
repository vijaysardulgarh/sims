# result_generations - urls.py
from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ResultGenerationViewSet
)

router = DefaultRouter()

router.register(
    "",
    ResultGenerationViewSet,
    basename="result-generation",
)

urlpatterns = router.urls