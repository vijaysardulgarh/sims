from django.shortcuts import render

from apps.academics.models import (
    Subject,
    ClassSubject
)


# =========================================
# SUBJECT LIST
# =========================================

def subject_list_view(request):

    subjects = Subject.objects.all()

    return render(
        request,
        "academics/subjects/list.html",
        {
            "subjects": subjects
        }
    )


# =========================================
# CLASS SUBJECT LIST
# =========================================

def class_subject_list_view(request):

    class_subjects = (
        ClassSubject.objects.select_related(
            "class_obj",
            "stream",
            "subject"
        )
    )

    return render(
        request,
        "academics/class_subjects/list.html",
        {
            "class_subjects": class_subjects
        }
    )