from django.shortcuts import render
import os
from django.conf import settings
from django.http import FileResponse, Http404

def admission_form(request):
    """Serve Admission Form PDF"""
    file_path = os.path.join(settings.BASE_DIR, "static", "admission_form.pdf")
    try:
        return FileResponse(open(file_path, "rb"), content_type="application/pdf")
    except FileNotFoundError:
        raise Http404("Admission form not found.")
    

def gallery(request): 
    return render(request, "gallery.html")

def notices(request): 
    return render(request, "notices.html")

def events(request): 
    return render(request, "events.html")    

def syllabus(request): 
    return render(request, "syllabus.html")

def management(request): return render(request, "management.html")
def curriculum(request): return render(request, "curriculum.html")
def exams_results(request): return render(request, "exams.html")
def academic_calendar(request): return render(request, "calendar.html")
def downloads(request): return render(request, "downloads.html")
def admission_procedure(request): return render(request, "admission_procedure.html")
def statistics(request): return render(request, "statistics.html")
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

