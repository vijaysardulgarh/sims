from rest_framework.routers import DefaultRouter

from .views import (
    CommunicationTemplateViewSet
)

router = DefaultRouter()

router.register(
    r'',
    CommunicationTemplateViewSet,
    basename='communication-template'
)

urlpatterns = router.urls