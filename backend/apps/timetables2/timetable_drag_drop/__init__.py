from apps.academics.timetable.timetables.models import (
    Timetable
)

from .serializers import (
    TimetableSerializer
)

from .views import (
    TimetableDragAPIView,
    TimetableUpdateAPIView,
    TimetableRemoveAPIView,
)