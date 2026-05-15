from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from apps.academics.timetables import (
    Timetable
)

from backend.apps.academics.reports.timetable_entry.serializers import (
    TimetableEntryReportSerializer
)


# =========================================
# TIMETABLE ENTRY REPORT API
# =========================================

class TimetableEntryReportAPIView(
    APIView
):

    def get(self, request):

        queryset = (

            Timetable.objects

            .select_related(

                "slot",

                "slot__day",

                "classroom",

                "teacher_subject_assignment",

                "teacher_subject_assignment__teacher",

                "teacher_subject_assignment__section",

                "teacher_subject_assignment__class_subject",

                "teacher_subject_assignment"
                "__class_subject__subject",
            )
        )

        data = []

        for item in queryset:

            data.append({

                "period":
                    item.slot.period_number,

                "teacher":
                    str(item.teacher),

                "subject":
                    str(
                        item.class_subject.subject
                    ),

                "section":
                    str(item.section),

                "classroom":
                    (
                        str(item.classroom)
                        if item.classroom
                        else None
                    ),

                "day":
                    (
                        item.slot.day.name
                        if item.slot.day
                        else None
                    ),
            })

        serializer = (

            TimetableEntryReportSerializer(
                data,
                many=True
            )
        )

        return Response(
            serializer.data
        )