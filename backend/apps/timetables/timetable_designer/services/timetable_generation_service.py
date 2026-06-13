from apps.timetables.period_definitions.models import (
    PeriodDefinition
)

from apps.timetables.timetable_entries.models import (
    TimetableEntry
)


class TimetableGenerationService:

    DAYS = [
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",
    ]

    @classmethod
    def generate(
        cls,
        timetable
    ):

        periods = (
            PeriodDefinition.objects
            .filter(
                is_active=True
            )
            .order_by(
                "display_order"
            )
        )

        created_count = 0

        for day in cls.DAYS:

            for period in periods:

                _, created = (
                    TimetableEntry.objects.get_or_create(
                        timetable=timetable,
                        day=day,
                        period=period,
                        defaults={
                            "remarks": ""
                        }
                    )
                )

                if created:
                    created_count += 1

        return {
            "created_entries": created_count,
            "total_entries": (
                TimetableEntry.objects.filter(
                    timetable=timetable
                ).count()
            )
        }