from django.shortcuts import render

from apps.academics.subjects import (
    Subject
)


def subject_list_view(request):

    subjects = (
        Subject.objects.all()
    )

    return render(

        request,

        "academics/subjects/list.html",

        {
            "subjects": subjects
        }
    )