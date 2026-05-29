from rest_framework.routers import DefaultRouter

from apps.timetables.class_subjects.views import (
    ClassSubjectViewSet
)

router = DefaultRouter()

router.register(
    r"class-subjects",
    ClassSubjectViewSet,
    basename="class-subject"
)

urlpatterns = router.urls