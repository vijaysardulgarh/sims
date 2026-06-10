# grade_scales - urls.py
from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    GradeScaleViewSet
)

router = DefaultRouter()

router.register(
    "",
    GradeScaleViewSet,
    basename="grade-scale",
)

urlpatterns = router.urls