from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from django.shortcuts import (
    get_object_or_404
)

from apps.academics.sections.models import (
    Section
)

from apps.academics.timetable_slots.models import (
    TimetableSlot
)

from apps.academics.timetables.models import (
    Timetable
)

from apps.academics.teacher_subject_assignments.models import (
    TeacherSubjectAssignment
)


class TimetableDragAPIView(
    APIView
):

    def get(self, request):

        sections = (
            Section.objects.all()
        )

        assignments = (

            TeacherSubjectAssignment.objects

            .select_related(
                "teacher",
                "class_subject__subject",
                "section"
            )
        )

        slots = (

            TimetableSlot.objects

            .select_related(
                "day"
            )
        )

        return Response({

            "sections":
                list(
                    sections.values(
                        "id",
                        "name"
                    )
                ),

            "assignments":
                list(
                    assignments.values(
                        "id",
                        "teacher__name",
                        "section__name",
                        "class_subject__subject__name"
                    )
                ),

            "slots":
                list(
                    slots.values(
                        "id",
                        "day__name",
                        "period_number"
                    )
                ),
        })


class TimetableUpdateAPIView(
    APIView
):

    def post(self, request):

        data = request.data

        tsa = get_object_or_404(

            TeacherSubjectAssignment,

            id=data["entry_id"]
        )

        slot = get_object_or_404(

            TimetableSlot,

            day_id=data["day"],

            period_number=data["period"]
        )

        Timetable.objects.update_or_create(

            teacher_subject_assignment=tsa,

            defaults={
                "slot": slot
            }
        )

        return Response({
            "success": True
        })


class TimetableRemoveAPIView(
    APIView
):

    def post(self, request):

        tsa = get_object_or_404(

            TeacherSubjectAssignment,

            id=request.data["entry_id"]
        )

        Timetable.objects.filter(

            teacher_subject_assignment=tsa

        ).delete()

        return Response({
            "success": True
        })