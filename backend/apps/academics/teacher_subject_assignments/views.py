from django.shortcuts import render

from apps.staff.models import (
    Staff
)

from apps.academics.sections import (
    Section
)

from apps.academics.class_subjects import (
    ClassSubject
)

from apps.academics.teacher_subject_assignments import (
    TeacherSubjectAssignment
)


def teacher_assignment_view(request):

    teachers = (

        Staff.objects.filter(
            staff_role="Teaching"
        )
    )

    sections = (
        Section.objects.all()
    )

    subjects = (

        ClassSubject.objects

        .select_related(
            "subject"
        )
    )

    assignments = (

        TeacherSubjectAssignment.objects

        .select_related(
            "teacher",
            "class_subject__subject",
            "section"
        )
    )

    return render(

        request,

        "academics/timetable/"
        "teacher_assignment.html",

        {
            "teachers": teachers,

            "sections": sections,

            "subjects": subjects,

            "assignments": assignments,
        }
    )