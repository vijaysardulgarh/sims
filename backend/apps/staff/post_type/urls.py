from rest_framework.routers import DefaultRouter

from .views import PostTypeViewSet


router = DefaultRouter()

router.register(
    "",
    PostTypeViewSet,
    basename="post-types"
)

urlpatterns = router.urls