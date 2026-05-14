from django.shortcuts import render

from apps.academics.sections import (
    Section
)

from apps.academics.teacher_subject_assignments import (
    TeacherSubjectAssignment
)

from apps.academics.timetable_slots import (
    TimetableSlot
)


def timetable_generate_view(request):

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

    return render(

        request,

        "academics/timetable/generate.html",

        {
            "sections": sections,

            "assignments": assignments,

            "slots": slots,
        }
    )