from django.urls import (
    path
)

from apps.academics.timetable.timetable_drag_drop.views import (
    TimetableDragAPIView,
    TimetableUpdateAPIView,
    TimetableRemoveAPIView,
)

urlpatterns = [

    path(
        "",
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