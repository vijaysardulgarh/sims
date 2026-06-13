from django.db import transaction

from apps.timetables.period_definitions.models import (
    PeriodDefinition,
)

from apps.timetables.timetable_entries.models import (
    TimetableEntry,
)


class TimetableMoveService:

    @staticmethod
    @transaction.atomic
    def move_entry(

        entry_id,
        target_day,
        target_period_order,

    ):

        source_entry = (

            TimetableEntry.objects.select_for_update()

            .get(
                id=entry_id
            )

        )

        target_period = (

            PeriodDefinition.objects.get(
                display_order=
                target_period_order
            )

        )

        target_entry = (

            TimetableEntry.objects.select_for_update()

            .filter(

                timetable=
                source_entry.timetable,

                day=
                target_day,

                period=
                target_period,

            )

            .first()

        )

        if not target_entry:

            source_entry.day = (
                target_day
            )

            source_entry.period = (
                target_period
            )

            source_entry.save()

            return

        source_day = (
            source_entry.day
        )

        source_period = (
            source_entry.period
        )

        source_entry.day = (
            "SUN"
        )

        source_entry.save()

        target_entry.day = (
            source_day
        )

        target_entry.period = (
            source_period
        )

        target_entry.save()

        source_entry.day = (
            target_day
        )

        source_entry.period = (
            target_period
        )

        source_entry.save()