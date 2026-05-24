from django.urls import (
    path
)

from apps.academics.timetable.timetable_generator.views import (
    TimetableGenerateAPIView
)

urlpatterns = [

    path(
        "",
        TimetableGenerateAPIView.as_view(),
        name="timetable-generate"
    ),
]