# exam_types - urls.py
from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    ExamTypeViewSet
)

router = DefaultRouter()

router.register(
    "",
    ExamTypeViewSet,
    basename="exam-type"
)

urlpatterns = router.urls