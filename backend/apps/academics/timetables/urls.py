from django.urls import (
    path
)

from apps.academics.timetables.views import (
    TimetableGenerateAPIView,
    TimetableDragAPIView,
    TimetableUpdateAPIView,
    TimetableRemoveAPIView,
)

urlpatterns = [

    path(
        "generate/",
        TimetableGenerateAPIView.as_view(),
        name="timetable-generate"
    ),

    path(
        "drag/",
        TimetableDragAPIView.as_view(),
        name="timetable-drag"
    ),

    path(
        "update/",
        TimetableUpdateAPIView.as_view(),
        name="timetable-update"
    ),

    path(
        "remove/",
        TimetableRemoveAPIView.as_view(),
        name="timetable-remove"
    ),
]