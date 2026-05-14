from django.shortcuts import render

from apps.academics.days import (
    Day
)


def day_list_view(request):

    days = (
        Day.objects.all()
    )

    return render(

        request,

        "academics/timetable/days.html",

        {
            "days": days
        }
    )