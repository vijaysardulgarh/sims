from rest_framework.routers import (
    DefaultRouter
)

from apps.library.accessions.views import (
    BookAccessionViewSet
)

router = DefaultRouter()

router.register(
    r"",
    BookAccessionViewSet,
    basename="book-accession"
)

urlpatterns = router.urls