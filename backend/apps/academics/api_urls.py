from django.urls import path, include

from rest_framework.routers import (
    DefaultRouter
)

from apps.academics.api.timetable_api import (

    DayViewSet,

    TimetableSlotViewSet,

    TimetableViewSet,

    TimetableGenerateAPIView,

    TeacherAssignmentAPIView,

    TimetableListAPIView,

    TeacherWorkloadAPIView,
)

router = DefaultRouter()

router.register(
    r"days",
    DayViewSet
)

router.register(
    r"timetable-slots",
    TimetableSlotViewSet
)

router.register(
    r"timetable",
    TimetableViewSet
)

urlpatterns = [

    path(
        "",
        include(router.urls)
    ),

    path(
        "generate/",
        TimetableGenerateAPIView.as_view()
    ),

    path(
        "teacher-assignment/",
        TeacherAssignmentAPIView.as_view()
    ),

    path(
        "timetable-list/",
        TimetableListAPIView.as_view()
    ),

    path(
        "teacher-workload/",
        TeacherWorkloadAPIView.as_view()
    ),
]