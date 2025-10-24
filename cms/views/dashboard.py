from django.shortcuts import render, redirect
from ..models.school import School


def sims_index(request):
    if 'clear' in request.GET:
        request.session.pop('school_id', None)
        return redirect('/')

    schools = School.objects.all()

    if request.method == "POST":
        school_id = request.POST.get("school")
        if school_id:
            request.session["school_id"] = int(school_id)
            return redirect("/index/")

    context = {
        "schools": schools
    }
    return render(request, "sims_index.html", context)

def index(request):
    selected_school_id = request.session.get("school_id")
    selected_school = None
    if selected_school_id:
        selected_school = School.objects.filter(id=selected_school_id).first()

    context = {
        "selected_school": selected_school,
    }
    return render(request, "index.html", context)