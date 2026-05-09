from django.shortcuts import render

from apps.academics.models import (
    Class,
    Stream,
    Medium,
    Classroom,
    Section
)


# =========================================
# CLASS LIST
# =========================================

def class_list_view(request):

    classes = Class.objects.all()

    return render(
        request,
        "academics/classes/list.html",
        {
            "classes": classes
        }
    )


# =========================================
# STREAM LIST
# =========================================

def stream_list_view(request):

    streams = Stream.objects.all()

    return render(
        request,
        "academics/streams/list.html",
        {
            "streams": streams
        }
    )


# =========================================
# MEDIUM LIST
# =========================================

def medium_list_view(request):

    mediums = Medium.objects.all()

    return render(
        request,
        "academics/mediums/list.html",
        {
            "mediums": mediums
        }
    )


# =========================================
# CLASSROOM LIST
# =========================================

def classroom_list_view(request):

    classrooms = Classroom.objects.all()

    return render(
        request,
        "academics/classrooms/list.html",
        {
            "classrooms": classrooms
        }
    )


# =========================================
# SECTION LIST
# =========================================

def section_list_view(request):

    sections = (
        Section.objects.select_related(
            "class_obj",
            "stream",
            "medium",
            "classroom"
        )
    )

    return render(
        request,
        "academics/sections/list.html",
        {
            "sections": sections
        }
    )