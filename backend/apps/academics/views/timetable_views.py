from django.shortcuts import render

from apps.staff.models import (
    Staff,
    TeacherSubjectAssignment
)

from apps.academics.models import (
    Day,
    TimetableSlot,
    Timetable,
    Section,
    ClassSubject
)


# =========================================
# DAY LIST
# =========================================

def day_list_view(request):

    days = Day.objects.all()

    return render(
        request,
        "academics/timetable/days.html",
        {
            "days": days
        }
    )


# =========================================
# SLOT LIST
# =========================================

def timetable_slot_list_view(request):

    slots = (
        TimetableSlot.objects.select_related(
            "day"
        )
    )

    return render(
        request,
        "academics/timetable/slots.html",
        {
            "slots": slots
        }
    )


# =========================================
# TIMETABLE LIST
# =========================================

def timetable_list_view(request):

    timetables = (
        Timetable.objects.select_related(
            "teacher_subject_assignment__teacher",
            "teacher_subject_assignment__class_subject__subject",
            "teacher_subject_assignment__section",
            "slot",
        )
    )

    return render(
        request,
        "academics/timetable/list.html",
        {
            "timetables": timetables
        }
    )


# =========================================
# TIMETABLE GENERATOR
# =========================================

def timetable_generate_view(request):

    sections = Section.objects.all()

    assignments = (
        TeacherSubjectAssignment.objects.select_related(
            "teacher",
            "class_subject__subject",
            "section"
        )
    )

    slots = (
        TimetableSlot.objects.select_related(
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


# =========================================
# TEACHER ASSIGNMENT
# =========================================

def teacher_assignment_view(request):

    teachers = Staff.objects.filter(
        staff_role="Teaching"
    )

    sections = Section.objects.all()

    subjects = (
        ClassSubject.objects.select_related(
            "subject"
        )
    )

    assignments = (
        TeacherSubjectAssignment.objects.select_related(
            "teacher",
            "class_subject__subject",
            "section"
        )
    )

    return render(
        request,
        "academics/timetable/teacher_assignment.html",
        {
            "teachers": teachers,
            "sections": sections,
            "subjects": subjects,
            "assignments": assignments,
        }
    )


# =========================================
# DRAG DROP TIMETABLE
# =========================================

def timetable_drag_view(request):

    sections = Section.objects.all()

    assignments = (
        TeacherSubjectAssignment.objects.select_related(
            "teacher",
            "class_subject__subject",
            "section"
        )
    )

    slots = (
        TimetableSlot.objects.select_related(
            "day"
        )
    )

    return render(
        request,
        "academics/timetable/drag_drop.html",
        {
            "sections": sections,
            "assignments": assignments,
            "slots": slots,
        }
    )