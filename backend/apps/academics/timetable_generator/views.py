from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from apps.core.utils.helpers import (
    get_current_school
)

from apps.staff.staff.models import (
    Staff
)

from apps.academics.classes.models import (
    Class
)

from apps.academics.subjects.models import (
    Subject
)

from apps.academics.timetable_slots.models import (
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

            .order_by(
                "class_order"
            )
        )

        subjects = (

            Subject.objects.filter(
                school=school
            )

            .order_by(
                "name"
            )
        )

        teachers = (

            Staff.objects.filter(
                school=school,
                staff_role="Teaching"
            )

            .order_by(
                "name"
            )
        )

        time_slots = (

            TimetableSlot.objects

            .filter(
                school=school
            )

            .select_related(
                "day"
            )

            .order_by(
                "day__sequence",
                "period_number"
            )
        )

        return Response({

            "classes":
                list(
                    classes.values(
                        "id",
                        "name"
                    )
                ),

            "subjects":
                list(
                    subjects.values(
                        "id",
                        "name",
                        "code"
                    )
                ),

            "teachers":
                list(
                    teachers.values(
                        "id",
                        "name"
                    )
                ),

            "time_slots":
                list(

                    time_slots.values(

                        "id",

                        "day__name",

                        "period_number"
                    )
                ),
        })