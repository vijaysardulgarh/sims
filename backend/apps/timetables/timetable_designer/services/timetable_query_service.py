from apps.timetables.timetable_entries.models import (
    TimetableEntry
)


class TimetableQueryService:

    @staticmethod
    def teacher_schedule(
        teacher_id
    ):

        return (
            TimetableEntry.objects.filter(
                teacher_id=teacher_id
            )
        )

    @staticmethod
    def room_schedule(
        room_id
    ):

        return (
            TimetableEntry.objects.filter(
                room_id=room_id
            )
        )

    @staticmethod
    def class_schedule(
        class_id
    ):

        return (
            TimetableEntry.objects.filter(
                school_class_id=class_id
            )
        )