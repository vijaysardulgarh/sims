from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.academics.structure.classes.models import (
    Class
)

from apps.academics.curriculum.subjects.models import (
    Subject
)

from apps.academics.timetable.timetable_slots.models import (
    TimetableSlot
)

from apps.staff.profiles.models import (
    Staff
)


# ==========================================
# TIMETABLE GENERATE API VIEW
# ==========================================

class TimetableGenerateAPIView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # ======================================
    # GET
    # ======================================

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        # ==================================
        # SCHOOL CHECK
        # ==================================

        if not school:

            return Response(

                {

                    "success": False,

                    "message":
                    "School not found."
                },

                status=400
            )

        # ==================================
        # CLASSES
        # ==================================

        classes = (

            Class.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("name")
        )

        # ==================================
        # SUBJECTS
        # ==================================

        subjects = (

            Subject.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("name")
        )

        # ==================================
        # TEACHERS
        # ==================================

        teachers = (

            Staff.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("name")
        )

        # ==================================
        # TIME SLOTS
        # ==================================

        time_slots = (

            TimetableSlot.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .select_related(
                "day"
            )

            .order_by(
                "day__display_order",
                "period_number"
            )
        )

        # ==================================
        # RESPONSE
        # ==================================

        return Response(

            {

                "success": True,

                "school": {

                    "id": school.id,

                    "name": school.name,
                },

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
            }
        )