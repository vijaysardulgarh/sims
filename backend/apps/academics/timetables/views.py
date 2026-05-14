from django.shortcuts import render

from apps.academics.timetables import (
    Timetable
)


def timetable_list_view(request):

    timetables = (

        Timetable.objects

        .select_related(
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
            "timetables":
                timetables
        }
    )