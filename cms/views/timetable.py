from django.shortcuts import render, get_object_or_404, redirect
from cms.utils import get_current_school
from ..models.staff import Staff,TeacherSubjectAssignment
from ..models.subject import Subject,ClassSubject
from ..models.schoolclass import Class,Section,Classroom
from ..models.timetable import Day,TimetableSlot,Timetable
from collections import defaultdict
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from cms.utils import generate_timetable
import json
from django.db.models import Count

def timetable_view(request):
    school = get_current_school(request)
    if not school:
        return redirect("select_school")

    classes = Class.objects.filter(school=school)
    subjects = Subject.objects.filter(school=school)
    teachers = Staff.objects.filter(school=school)
    time_slots = TimetableSlot.objects.filter(school=school)

    total_duration = 5 * 8  # 5 days × 8 hours

    timetable = generate_timetable(classes, subjects, teachers, time_slots, total_duration)

    context = {
        "timetable": timetable,
        "classes": classes,
        "subjects": subjects,
        "teachers": teachers,
        "time_slots": time_slots,
    }
    return render(request, "timetable/timetable.html", context)


def teacher_subject_section_assignment(request):
    teachers_qs = Staff.objects.filter(staff_role="Teaching").select_related("post_type")

    def sort_post_type(post_type_name):
        if post_type_name == "TGT":
            return 0
        elif post_type_name == "PGT":
            return 1
        else:
            return 2

    teachers = sorted(
        teachers_qs,
        key=lambda t: (
            sort_post_type(t.post_type.name if t.post_type else ''),
            t.post_type.name if t.post_type else '',
            t.name
        )
    )

    sections_qs = Section.objects.select_related("sec_class", "stream", "medium").all().order_by("sec_class__class_order", "name")
    sections = {sec.id: sec for sec in sections_qs}

    class_subjects_qs = ClassSubject.objects.select_related("subject_class", "subject").all()
    class_subjects = {cs.id: cs for cs in class_subjects_qs}

    # Existing assignments lookup
    teacher_assignments = {}
    for tsa in TeacherSubjectAssignment.objects.all():
        teacher_assignments.setdefault(tsa.teacher_id, {})
        teacher_assignments[tsa.teacher_id].setdefault(tsa.section_id, [])
        teacher_assignments[tsa.teacher_id][tsa.section_id].append(tsa.class_subject_id)

    if request.method == "POST":
        for teacher in teachers:
            teacher_prefix = f"teacher_{teacher.id}_section_"
            section_keys = [k for k in request.POST.keys() if k.startswith(teacher_prefix) and "_subjects" not in k]

            for section_key in section_keys:
                section_id = request.POST[section_key]
                subject_ids = request.POST.getlist(f"{section_key}_subjects")

                # Remove existing assignments
                TeacherSubjectAssignment.objects.filter(
                    teacher=teacher,
                    section_id=section_id
                ).delete()

                # Create new assignments
                for subj_id in subject_ids:
                    TeacherSubjectAssignment.objects.create(
                        teacher=teacher,
                        section_id=section_id,
                        class_subject_id=subj_id
                    )

        return redirect("teacher_subject_section_assignment")

    context = {
        "teachers": teachers,
        "sections": sections,
        "class_subjects": class_subjects,
        "teacher_assignments": teacher_assignments,
    }
    return render(request, "timetable/teacher_subject_section_assignment.html", context)


# AJAX view for filtering subjects by section
def get_subjects_for_section(request):
    section_id = request.GET.get('section_id')
    subjects = []

    if section_id:
        try:
            section = Section.objects.select_related("sec_class", "stream").get(id=section_id)

            # Filter ClassSubject by class, stream, sub_stream
            class_subjects = ClassSubject.objects.filter(
                subject_class=section.sec_class,
                stream=section.stream if section.stream else None,
                sub_stream=section.sub_stream if section.sub_stream else None
            )

            for cs in class_subjects:
                subjects.append({"id": cs.id, "name": cs.subject.name})
        except Section.DoesNotExist:
            pass

    return JsonResponse({"subjects": subjects})



def create_timetable_entry(request):
    teachers = TeacherSubjectAssignment.objects.select_related("teacher").all()
    classrooms = Classroom.objects.all()
    substitute_teachers = Staff.objects.filter(staff_role="Teaching")

    # Define available days & periods
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    periods = range(1, 8)  # 1–7

    if request.method == "POST":
        # Find which teacher form was submitted
        teacher_id = None
        for t in teachers:
            if f"days_{t.id}" in request.POST:
                teacher_id = t.id
                break

        if teacher_id:
            teacher_assignment = TeacherSubjectAssignment.objects.get(id=teacher_id)

            # Selected values
            selected_days = request.POST.getlist(f"days_{teacher_id}")
            selected_periods = request.POST.getlist(f"periods_{teacher_id}")
            classroom_id = request.POST.get(f"classroom_{teacher_id}")
            substitute_id = request.POST.get(f"substitute_teacher_{teacher_id}")

            classroom = Classroom.objects.filter(id=classroom_id).first() if classroom_id else None
            substitute_teacher = Staff.objects.filter(id=substitute_id).first() if substitute_id else None

            # Save timetable entries
            for day in selected_days:
                for period in selected_periods:
                    Timetable.objects.create(
                        teacher_assignment=teacher_assignment,
                        slot_day=day,       # adjust if you use a related `Day` model
                        slot_period=period, # adjust if you use a `Slot` model
                        classroom=classroom,
                        substitute_teacher=substitute_teacher,
                    )

            messages.success(request, f"Timetable saved for {teacher_assignment.teacher}")
            return redirect("timetable_list")

    return render(request, "timetable/create_timetable.html", {
        "teachers": teachers,
        "classrooms": classrooms,
        "substitute_teachers": substitute_teachers,
        "days": days,
        "periods": periods,
        "school": {"name": "PM Shri Government Senior Secondary School Nagpur"},
    })



def timetable_list(request):
    timetables = Timetable.objects.select_related(
        'teacher_assignment',
        'teacher_assignment__teacher',
        'teacher_assignment__class_subject',
        'teacher_assignment__section',
        'slot',
        'slot__day'
    ).all()

    # Group timetables by day name
    grouped_timetables = defaultdict(list)
    for t in timetables:
        grouped_timetables[t.slot.day.name].append(t)

    periods = range(1, 8)  # 7 periods

    # Get all days in sequence for the school of the first timetable, or default
    if timetables.exists():
        school = timetables.first().school
        days = Day.objects.filter(school=school).order_by('sequence')
    else:
        days = []

    return render(request, "timetable/timetable_list.html", {
        "grouped_timetables": grouped_timetables,
        "periods": periods,
        "days": days,
    })




def reports_dashboard(request):
    # Fetch all sections and teachers for dropdowns
    sections = Section.objects.select_related("sec_class").order_by("sec_class__name", "name")
    teachers = Staff.objects.filter(staff_role="Teaching").order_by("name")

    section_id = request.GET.get("section")
    teacher_id = request.GET.get("teacher")

    section_report_data = {}
    teacher_report_data = {}
    teacher_workload_data = []
    subject_section_report_data = []
    subject_overall_load_data = []

    # Section-wise timetable report
    if section_id:
        section_id = int(section_id)
        section_report_data = section_timetable_report(
            section_id,
            teacher_id=int(teacher_id) if teacher_id else None
        )

    # Teacher-wise timetable report
    if teacher_id:
        teacher_id = int(teacher_id)
        teacher_report_data = teacher_timetable_report(teacher_id)

    # Teacher workload across all sections
    teacher_workload_data = teacher_workload_report()

    # Subject/section-wise period count
    subject_section_report_data = subject_section_period_report()

    # Subject-wise overall load
    subject_overall_load_data = subject_overall_load_report()

    context = {
        "sections": sections,
        "teachers": teachers,
        "selected_section": int(section_id) if section_id else None,
        "selected_teacher": int(teacher_id) if teacher_id else None,
        "section_report": section_report_data,
        "teacher_report": teacher_report_data,
        "teacher_workload_report": teacher_workload_data,
        "subject_section_report": subject_section_report_data,
        "subject_overall_load_report": subject_overall_load_data,
    }

    return render(request, "timetable/dashboard.html", context)


# ---------- Helper functions ----------

def section_timetable_report(section_id, teacher_id=None):
    """
    Returns timetable for a section.
    If teacher_id is provided, filters only that teacher; otherwise, includes all teachers in that section.
    """
    entries = Timetable.objects.filter(teacher_assignment__section_id=section_id)

    if teacher_id:
        entries = entries.filter(teacher_assignment__teacher_id=teacher_id)

    entries = entries.select_related(
        "teacher_assignment__teacher",
        "teacher_assignment__class_subject__subject",
        "teacher_assignment__section__sec_class",
        "slot",
        "classroom"
    ).order_by("slot__day__sequence", "slot__period_number")

    timetable = defaultdict(list)
    for e in entries:
        timetable[e.slot.day.name].append({
            "period": e.slot.period_number,
            "subject": e.teacher_assignment.class_subject.subject.name,
            "teacher": e.teacher_assignment.teacher.name,
            "class_name": e.teacher_assignment.section.sec_class.name,
            "section_name": e.teacher_assignment.section.name,
            "classroom": e.classroom.name if e.classroom else None,
        })
    return dict(timetable)


def teacher_timetable_report(teacher_id):
    entries = (
        Timetable.objects.filter(teacher_assignment__teacher_id=teacher_id)
        .select_related(
            "teacher_assignment__section",
            "teacher_assignment__section__sec_class",
            "teacher_assignment__class_subject__subject",
            "slot",
            "classroom"
        )
        .order_by("slot__day__sequence", "slot__period_number")
    )

    timetable = defaultdict(list)
    for e in entries:
        timetable[e.slot.day.name].append({
            "period": e.slot.period_number,
            "subject": e.teacher_assignment.class_subject.subject.name,
            "class_name": e.teacher_assignment.section.sec_class.name,
            "section_name": e.teacher_assignment.section.name,
            "classroom": e.classroom.name if e.classroom else None,
        })
    return dict(timetable)


def teacher_workload_report():
    return (
        Timetable.objects.values(
            "teacher_assignment__teacher__id",
            "teacher_assignment__teacher__name"
        )
        .annotate(total_periods=Count("id"))
        .order_by("teacher_assignment__teacher__name")
    )


def subject_section_period_report():
    return (
        Timetable.objects.values(
            "teacher_assignment__section__sec_class__name",
            "teacher_assignment__section__name",
            "teacher_assignment__class_subject__subject__name"
        )
        .annotate(periods_assigned=Count("id"))
        .order_by(
            "teacher_assignment__section__sec_class__name",
            "teacher_assignment__section__name",
            "teacher_assignment__class_subject__subject__name"
        )
    )


def subject_overall_load_report():
    """
    Returns total periods assigned for each subject across all sections.
    """
    return (
        Timetable.objects.values(
            "teacher_assignment__class_subject__subject__name"
        )
        .annotate(total_periods=Count("id"))
        .order_by("teacher_assignment__class_subject__subject__name")
    )





def timetable_dragndrop(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # Multi-section selection
    section_ids = request.GET.getlist("sections")
    if section_ids:
        sections = Section.objects.filter(id__in=section_ids)
    else:
        sections = Section.objects.filter(sec_class__school=school)

    # Teacher-Subject assignments for selected sections
    assignments = TeacherSubjectAssignment.objects.filter(section__in=sections).select_related(
        "teacher",
        "class_subject__subject",
        "section__sec_class",
        "section__classroom"
    )

    # Current timetable entries
    timetable_entries = Timetable.objects.filter(
        teacher_assignment__section__in=sections
    ).select_related(
        "teacher_assignment__teacher",
        "teacher_assignment__class_subject__subject",
        "slot",
        "classroom",
        "teacher_assignment__section__sec_class"
    )

    # Build lookup dict: timetable_lookup[day][period][section_id] = entries
    timetable_lookup = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for entry in timetable_entries:
        day_id = entry.slot.day.id
        period = entry.slot.period_number or 0
        timetable_lookup[day_id][period][entry.teacher_assignment.section.id].append(entry)

    # Period numbers
    period_numbers = list(
        TimetableSlot.objects.filter(school=school)
        .values_list("period_number", flat=True)
        .distinct()
        .order_by("period_number")
    )

    # Compute workloads
    teacher_loads = defaultdict(int)
    subject_loads = defaultdict(int)

    all_teachers = [a.teacher for a in assignments]
    for entry in Timetable.objects.filter(teacher_assignment__teacher__in=all_teachers):
        teacher_loads[entry.teacher_assignment.teacher.id] += 1

    for entry in timetable_entries:
        subject_loads[(entry.teacher_assignment.class_subject.id, entry.teacher_assignment.section.id)] += 1

    # Add workload info to assignments
    assignment_data = []
    for assign in assignments:
        assignment_data.append({
            "id": assign.id,
            "teacher": assign.teacher,
            "class_subject": assign.class_subject,
            "section": assign.section,
            "current_load": teacher_loads.get(assign.teacher.id, 0),
            "max_load": assign.teacher.max_periods_per_week,
            "current_subject_load": subject_loads.get((assign.class_subject.id, assign.section.id), 0),
            "required_subject_load": assign.class_subject.periods_per_week,
        })

    context = {
        "school": school,
        "sections": sections,
        "assignments": assignment_data,
        "days": Day.objects.filter(school=school).order_by("sequence"),
        "period_numbers": period_numbers,
        "timetable_lookup": timetable_lookup,
    }
    return render(request, "timetable/timetable_dragndrop.html", context)


@csrf_exempt
@require_POST
def timetable_update(request):
    try:
        data = json.loads(request.body)
        entry_id = data.get("entry_id")
        section_id = data.get("section_id")
        target_day = data.get("target_day")
        target_period = data.get("target_period")

        tsa = TeacherSubjectAssignment.objects.get(id=entry_id, section_id=section_id)

        slot = TimetableSlot.objects.get(
            day_id=target_day,
            period_number=target_period,
            school=tsa.section.sec_class.school
        )

        Timetable.objects.update_or_create(
            teacher_assignment=tsa,
            slot=slot,
            defaults={
                "classroom": tsa.section.classroom,
                "school": tsa.section.sec_class.school
            }
        )
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


@csrf_exempt
@require_POST
def timetable_remove(request):
    try:
        data = json.loads(request.body)
        entry_id = data.get("entry_id")
        section_id = data.get("section_id")
        tsa = TeacherSubjectAssignment.objects.get(id=entry_id, section_id=section_id)
        Timetable.objects.filter(teacher_assignment=tsa).delete()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
    

def time_table(request): 
    return render(request, "time_table.html")    

