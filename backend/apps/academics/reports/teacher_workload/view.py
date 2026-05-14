from django.shortcuts import render

from django.db.models import (
    Count
)

from apps.academics.timetables import (
    Timetable
)


def teacher_workload_view(request):

    data = (

        Timetable.objects

        .values(
            "teacher_subject_assignment"
            "__teacher__name"
        )

        .annotate(
            total=Count("id")
        )
    )

    return render(

        request,

        "academics/reports/"
        "teacher_workload.html",

        {
            "data": data
        }
    )