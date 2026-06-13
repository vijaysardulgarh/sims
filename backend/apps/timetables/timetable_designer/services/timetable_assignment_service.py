from apps.timetables.timetable_entries.models import (
    TimetableEntry
)


class TimetableAssignmentService:

    @staticmethod
    def assign_subject(
        entry_id,
        subject_id
    ):

        entry = (
            TimetableEntry.objects.get(
                id=entry_id
            )
        )

        entry.subject_id = subject_id

        entry.save(
            update_fields=[
                "subject"
            ]
        )

        return entry

    @staticmethod
    def assign_teacher(
        entry_id,
        teacher_id
    ):

        entry = (
            TimetableEntry.objects.get(
                id=entry_id
            )
        )

        entry.teacher_id = teacher_id

        entry.save(
            update_fields=[
                "teacher"
            ]
        )

        return entry

    @staticmethod
    def assign_room(
        entry_id,
        room_id
    ):

        entry = (
            TimetableEntry.objects.get(
                id=entry_id
            )
        )

        entry.room_id = room_id

        entry.save(
            update_fields=[
                "room"
            ]
        )

        return entry