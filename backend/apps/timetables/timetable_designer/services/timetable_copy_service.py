from apps.timetables.timetable_entries.models import (
    TimetableEntry
)


class TimetableCopyService:

    @staticmethod
    def copy_day(
        timetable_id,
        source_day,
        target_day
    ):

        entries = (
            TimetableEntry.objects.filter(
                timetable_id=timetable_id,
                day=source_day
            )
        )

        for entry in entries:

            entry.pk = None
            entry.day = target_day
            entry.save()

        return True