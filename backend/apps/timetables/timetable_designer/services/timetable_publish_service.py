class TimetablePublishService:

    @staticmethod
    def publish(
        timetable
    ):

        timetable.is_published = True

        timetable.save(
            update_fields=[
                "is_published"
            ]
        )

        return timetable