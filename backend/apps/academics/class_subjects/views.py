from django.shortcuts import render

from apps.academics.class_subjects import (
    ClassSubject
)


def class_subject_list_view(request):

    class_subjects = (

        ClassSubject.objects

        .select_related(
            "class_obj",
            "stream",
            "subject"
        )
    )

    return render(

        request,

        "academics/class_subjects/list.html",

        {
            "class_subjects":
                class_subjects
        }
    )