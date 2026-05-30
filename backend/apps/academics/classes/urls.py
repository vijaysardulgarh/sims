from rest_framework.routers import DefaultRouter

from apps.academics.classes.views import (
    ClassViewSet
)

router = DefaultRouter()

router.register(
    r"",
    ClassViewSet,
    basename="class"
)

urlpatterns = router.urls