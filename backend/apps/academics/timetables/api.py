from rest_framework import viewsets

from apps.academics.timetables import (
    Timetable
)

from apps.academics.timetables.serializer import (
    TimetableSerializer
)


class TimetableViewSet(
    viewsets.ModelViewSet
):

    queryset = (

        Timetable.objects

        .select_related(
            "teacher_subject_assignment__teacher",
            "teacher_subject_assignment__section",
            "teacher_subject_assignment__class_subject__subject",
            "slot",
            "classroom",
        )
    )

    serializer_class = (
        TimetableSerializer
    )