from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from django.shortcuts import (
    get_object_or_404
)

from apps.academics.sections import (
    Section
)

from apps.academics.timetable_slots import (
    TimetableSlot
)

from apps.academics.timetables import (
    Timetable
)

from apps.academics.teacher_subject_assignments import (
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
            .all()
        )

        return Response({

            "sections":
                list(sections.values()),

            "assignments":
                list(assignments.values())
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

            slot=slot
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