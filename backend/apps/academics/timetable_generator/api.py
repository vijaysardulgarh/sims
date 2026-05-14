from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from apps.core.utils.helpers import (
    get_current_school
)

from apps.staff.models import (
    Staff
)

from apps.academics.classes import (
    Class
)

from apps.academics.subjects import (
    Subject
)

from apps.academics.timetable_slots import (
    TimetableSlot
)


class TimetableGenerateAPIView(
    APIView
):

    def get(self, request):

        school = (
            get_current_school(request)
        )

        if not school:

            return Response({

                "error":
                    "School not selected"

            }, status=400)

        classes = (
            Class.objects.filter(
                school=school
            )
        )

        subjects = (
            Subject.objects.filter(
                school=school
            )
        )

        teachers = (
            Staff.objects.filter(
                school=school
            )
        )

        time_slots = (

            TimetableSlot.objects

            .filter(
                school=school
            )
        )

        return Response({

            "classes":
                list(classes.values()),

            "subjects":
                list(subjects.values()),

            "teachers":
                list(teachers.values()),

            "time_slots":
                list(time_slots.values()),
        })