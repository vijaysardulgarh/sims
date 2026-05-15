from rest_framework.routers import (
    DefaultRouter
)

from apps.library.categories.views import (
    BookCategoryViewSet
)

router = DefaultRouter()

router.register(
    r"",
    BookCategoryViewSet,
    basename="book-category"
)

urlpatterns = router.urls