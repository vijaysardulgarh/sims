from rest_framework.routers import DefaultRouter

from .views import (
    CommunicationCategoryViewSet
)

router = DefaultRouter()

router.register(
    r'communication-categories',
    CommunicationCategoryViewSet,
    basename='communication-category'
)

urlpatterns = router.urls