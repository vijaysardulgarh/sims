from django.shortcuts import render

from apps.academics.timetable_slots import (
    TimetableSlot
)


def timetable_slot_list_view(request):

    slots = (

        TimetableSlot.objects

        .select_related(
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