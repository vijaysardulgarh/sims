from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q, Case, When,Sum,OuterRef,IntegerField,Value,CharField
from django.http import FileResponse, Http404
from django.utils.timezone import now

from .utils import get_current_school
from .models import (
    Staff, Student, Class, Subject,MandatoryPublicDisclosure,Timetable,TimetableSlot,Classroom,Day,School,
    News, SMCMember, Committee, School,FeeStructure,FAQ,ClassSubject,Section,TeacherSubjectAssignment,TeacherAttendance,
    AboutSchool, Principal, Affiliation,StaffAssociationRoleAssignment, Association,StudentAchievement,Infrastructure,SanctionedPost
   
)
from collections import defaultdict
from cms.utils import generate_timetable
from django.core.exceptions import ValidationError
import itertools
from django.db.models import Prefetch
import os
from django.conf import settings
# -------------------- Utility --------------------
from django.db.models import F
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import Student
import io
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from reportlab.platypus import Spacer
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.dateparse import parse_date
from django.utils import timezone

# -------------------- Dashboard & Common --------------------
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


def contact(request):
    school = get_current_school(request)
    return render(request, "contact.html", {"school": school})


# -------------------- Academics --------------------

def timetable_view(request):
    school = get_current_school(request)
    if not school:
        return redirect("select_school")

    classes = Class.objects.filter(school=school)
    subjects = Subject.objects.filter(school=school)
    teachers = Staff.objects.filter(school=school)
    time_slots = TimeSlot.objects.filter(school=school)

    total_duration = 5 * 8  # 5 days × 8 hours

    timetable = generate_timetable(classes, subjects, teachers, time_slots, total_duration)

    context = {
        "timetable": timetable,
        "classes": classes,
        "subjects": subjects,
        "teachers": teachers,
        "time_slots": time_slots,
    }
    return render(request, "timetable.html", context)


def student_strength(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    class_order = {
        "Sixth": 1, "Seventh": 2, "Eighth": 3, "Nineth": 4,
        "Tenth": 5, "Eleventh": 6, "Twelfth": 7,
    }

    student_strength = Student.objects.filter(school_name=school.name).values(
        "studentclass", "section", "stream"
    ).annotate(
        scmale=Count("srn", filter=Q(gender="Male", category__in=["SC", "Scheduled Caste"])),
        scfemale=Count("srn", filter=Q(gender="Female", category__in=["SC", "Scheduled Caste"])),
        bcamale=Count("srn", filter=Q(gender="Male", category="BC-A")),
        bcafemale=Count("srn", filter=Q(gender="Female", category="BC-A")),
        bcbmale=Count("srn", filter=Q(gender="Male", category="BC-B")),
        bcbfemale=Count("srn", filter=Q(gender="Female", category="BC-B")),
        genmale=Count("srn", filter=Q(gender="Male", category="GEN")),
        genfemale=Count("srn", filter=Q(gender="Female", category="GEN")),
        totalmale=Count("srn", filter=Q(gender="Male")),
        totalfemale=Count("srn", filter=Q(gender="Female")),
        total=Count("srn"),
        malecwsn=Count("srn", filter=Q(gender="Male") & ~Q(disability=None) & ~Q(disability="")),
        femalecwsn=Count("srn", filter=Q(gender="Female") & ~Q(disability=None) & ~Q(disability="")),
        cwsn=Count("srn", filter=~Q(disability="") | ~Q(disability=None)),
        malebpl=Count("srn", filter=Q(gender="Male") & ~Q(bpl_certificate_issuing_authority=None) & ~Q(bpl_certificate_issuing_authority="")),
        femalebpl=Count("srn", filter=Q(gender="Female") & ~Q(bpl_certificate_issuing_authority=None) & ~Q(bpl_certificate_issuing_authority="")),
        bpl=Count("srn", filter=~Q(bpl_certificate_issuing_authority="") | ~Q(bpl_certificate_issuing_authority=None)),
        order=Case(*[When(studentclass=cls, then=pos) for cls, pos in class_order.items()])
    ).order_by("order")

    return render(request, "student_strength.html", {"student_strength": student_strength, "school": school})


def subject_strength(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    class_order = {
        "Sixth": 1, "Seventh": 2, "Eighth": 3, "Nineth": 4,
        "Tenth": 5, "Eleventh": 6, "Twelfth": 7,
    }

    subject_strength = Student.objects.filter(school_name=school.name).values(
        "studentclass", "section", "stream"
    ).annotate(
        punjabi=Count("srn", filter=Q(subjects_opted__icontains="Punjabi")),
        music=Count("srn", filter=Q(subjects_opted__icontains="Music")),
        accountancy=Count("srn", filter=Q(subjects_opted__icontains="Accountancy")),
        business_studies=Count("srn", filter=Q(subjects_opted__icontains="Business Studies")),
        economics=Count("srn", filter=Q(subjects_opted__icontains="Economics")),
        sanskrit=Count("srn", filter=Q(subjects_opted__icontains="Sanskrit")),
        fine_arts=Count("srn", filter=Q(subjects_opted__icontains="Fine Arts")),
        political_science=Count("srn", filter=Q(subjects_opted__icontains="Political Science")),
        geography=Count("srn", filter=Q(subjects_opted__icontains="Geography")),
        mathematics=Count("srn", filter=Q(subjects_opted__icontains="Mathematics")),
        psychology=Count("srn", filter=Q(subjects_opted__icontains="Psychology")),
        drawing=Count("srn", filter=Q(subjects_opted__icontains="Drawing")),
        english=Count("srn", filter=Q(subjects_opted__icontains="English")),
        hindi=Count("srn", filter=Q(subjects_opted__icontains="Hindi")),
        social_science=Count("srn", filter=Q(subjects_opted__icontains="Social Science")),
        science = Count("srn",filter=Q(subjects_opted__iregex=r"\bScience\b"))
        #science=Count("srn", filter=Q(subjects_opted__icontains="Science") & ~Q(subjects_opted__icontains="Political Science")& ~Q(subjects_opted__icontains="Computer Science") & ~Q(subjects_opted__icontains="Home Science")),
        physics=Count("srn", filter=Q(subjects_opted__icontains="Physics")),
        chemistry=Count("srn", filter=Q(subjects_opted__icontains="Chemistry")),
        biology=Count("srn", filter=Q(subjects_opted__icontains="Biology")),
        home_science=Count("srn", filter=Q(subjects_opted__icontains="Home Science")),
        physical_education=Count("srn", filter=Q(subjects_opted__icontains="Physical and Health Education") | Q(subjects_opted__icontains="Physical Education")),
        automobile=Count("srn", filter=Q(subjects_opted__icontains="Automotive")),
        beauty_wellness=Count("srn", filter=Q(subjects_opted__icontains="Beauty & Wellness")),
        computer_science=Count("srn", filter=Q(subjects_opted__icontains="Computer Science")),
        order=Case(*[When(studentclass=cls, then=pos) for cls, pos in class_order.items()])
    ).order_by("order")

    return render(request, "subject_strength.html", {"subject_strength": subject_strength, "school": school})


# -------------------- School Info --------------------

def about_school(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    about = AboutSchool.objects.filter(school=school).first()
    return render(request, "about_us/about.html", {"about": about})


def smc_members(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    smcmembers = SMCMember.objects.filter(school=school)
    return render(request, "about_us/smc_members.html", {"smcmembers": smcmembers})


def principal(request):
    school = get_current_school(request)
    message = Principal.objects.filter(school=school).first() if school else Principal.objects.first()
    return render(request, "about_us/principal.html", {"message": message})


def affiliation_status(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    affiliations = Affiliation.objects.filter(school=school)
    return render(request, "about_us/affiliation_status.html", {"school": school, "affiliations": affiliations})




def teacher_attendance(request):
    # Parse date (default to today)
    date_str = request.POST.get("date") or request.GET.get("date")
    date = parse_date(date_str) if date_str else timezone.now().date()
    if date is None:  # fallback if parse_date fails
        date = timezone.now().date()

    if request.method == "POST":
        # Clear old records for the date
        TeacherAttendance.objects.filter(date=date).delete()

        # Save new attendance
        for teacher in Staff.objects.filter(staff_role="Teaching"):
            present = request.POST.get(f"present_{teacher.id}") == "on"
            TeacherAttendance.objects.create(
                teacher=teacher,
                date=date,
                present=present
            )
        return redirect("teacher_attendance")

    # Teachers list
    teachers = Staff.objects.filter(staff_role="Teaching").order_by("name")

    # Existing records for that date
    attendance_records = {
        rec.teacher_id: rec for rec in TeacherAttendance.objects.filter(date=date)
    }

    # Attach record to each teacher object
    for teacher in teachers:
        teacher.attendance_record = attendance_records.get(teacher.id)

    return render(request, "teacher_attendance.html", {
        "teachers": teachers,
        "date": date,
    })


def teacher_attendance_update(request, pk):
    record = get_object_or_404(TeacherAttendance, pk=pk)
    if request.method == "POST":
        record.present = request.POST.get("present") == "on"
        record.save()
        return redirect("teacher_attendance")
    return render(request, "teacher_attendance_update.html", {"record": record})


def teacher_attendance_delete(request, pk):
    record = get_object_or_404(TeacherAttendance, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("teacher_attendance")
    return render(request, "teacher_attendance_delete.html", {"record": record})



# -------------------- Static Pages --------------------

def management(request): return render(request, "management.html")
def committee(request): return render(request, "about_us/committee.html")
def infrastructure(request): return render(request, "about_us/infrastructure.html")

def subjects_offered(request): return render(request, "subjects.html")
def curriculum(request): return render(request, "curriculum.html")
def syllabus(request): return render(request, "syllabus.html")
def exams_results(request): return render(request, "exams.html")
def academic_calendar(request): return render(request, "calendar.html")
def time_table(request): return render(request, "time_table.html")
def downloads(request): return render(request, "downloads.html")

def admin_staff(request): return render(request, "admin_staff.html")
def teaching_staff(request): return render(request, "teaching_staff.html")
def non_teaching_staff(request): return render(request, "non_teaching_staff.html")
def support_staff(request): return render(request, "support_staff.html")

def achievements(request): return render(request, "achievements.html")
def board_results(request): return render(request, "board_results.html")
def sports_achievements(request): return render(request, "sports.html")
def gallery(request): return render(request, "gallery.html")
def notices(request): return render(request, "notices.html")
def events(request): return render(request, "events.html")

def admission_procedure(request): return render(request, "admission_procedure.html")
def admission_form(request):
    """Serve Admission Form PDF"""
    file_path = os.path.join(settings.BASE_DIR, "static", "admission_form.pdf")
    try:
        return FileResponse(open(file_path, "rb"), content_type="application/pdf")
    except FileNotFoundError:
        raise Http404("Admission form not found.")
#def admission_form(request): return render(request, "admission_form.pdf")
def prospectus(request): return render(request, "prospectus.html")

# def fee_structure(request):
#     fee_data = FeeStructure.objects.all().order_by('student_class')
#     return render(request, "fee_structure.html", {"fee_data": fee_data})

def fee_structure_list(request):
    fee_structures = FeeStructure.objects.select_related("student_class", "stream", "student_class__school")
    return render(request, "fees_list.html", {"fee_structures": fee_structures})

#def fee_structure(request): return render(request, "fee_structure.html")
def faq(request):
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'category')
    # Optional: group by category
    categories = {}
    for faq in faqs:
        categories.setdefault(faq.get_category_display(), []).append(faq)
    return render(request, 'faq.html', {'categories': categories})
# def faq(request): return render(request, "faq.html")


def statistics(request): return render(request, "statistics.html")
def safety_committee(request): return render(request, "safety_committee.html")
def grievance_committee(request): return render(request, "grievance_committee.html")
def icc_committee(request): return render(request, "icc_committee.html")
def committee_list(request): return render(request, "committee_list.html")
def committee_detail(request): return render(request, "committee_detail.html")


# -------------------- Documents & Staff --------------------

def document_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    documents = school.documents.all()
    return render(request, "document_detail.html", {"school": school, "documents": documents})


def staff_by_role(request, role):
    staff_list = Staff.objects.filter(staff_role=role).order_by("name")
    return render(request, "staff_by_role.html", {"role": role, "staff_list": staff_list})

# def nodal_detail(request, pk):
#     school = get_current_school(request)

#     # if no school is selected from homepage/session → redirect back
#     if not school:
#         return redirect("/")

#     nodal = get_object_or_404(
#         Nodal.objects.select_related("school")
#         .prefetch_related("staff")
#         .filter(school=school),
#         pk=pk,
#     )
#     return render(request, "nodal_detail.html", {"nodal": nodal, "school": school})
def staff_association_roles(request):
    staff_members = Staff.objects.prefetch_related(
        "association_roles__role__association__type",
        "association_roles__role__association__school"
    ).all()

    context = {
        "staff_members": staff_members
    }
    return render(request, "staff_association_roles.html", context)

def nodal(request):
    school = get_current_school(request)

    if not school:
        return redirect("/")  # Ensure school is set in session

    # Only fetch nodal associations
    nodal_assignments = StaffAssociationRoleAssignment.objects.filter(
        role__association__type__name="Nodal",
        staff__school=school,
    ).select_related(
        "staff", "role", "role__association", "role__association__type"
    )

    # Get distinct staff with preloaded nodal assignments
    staff_members = Staff.objects.filter(
        association_roles__in=nodal_assignments
    ).prefetch_related(
        Prefetch("association_roles", queryset=nodal_assignments, to_attr="nodal_roles")
    ).distinct()

    return render(
        request,
        "about_us/nodal.html",   # ✅ renamed template
        {"staff_members": staff_members, "school": school},
    )

def infrastructure(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")  # if no school in session, send user back to homepage

    infrastructures = school.infrastructures.all().order_by("category")
    return render(request, "about_us/infrastructure.html", {
        "school": school,
        "infrastructures": infrastructures
    })


def committee_detail(request, pk):
    committee = get_object_or_404(
        Association.objects.prefetch_related("roles__assigned_staff__staff"),
        pk=pk,
        type__name="Committee"
    )
    return render(request, "committee_detail.html", {"committee": committee})


def staff_summary(request):
    school = get_object_or_404(School, id=request.session.get("school_id"))

    # Allowed post types in required order
    allowed_post_types = ["Principal", "PGT", "TGT", "Clerk", "Lab Attendent", "Class IV"]

    # 1. Fetch sanctioned posts
    sanctioned = (
        SanctionedPost.objects.filter(school=school, post_type__name__in=allowed_post_types)
        .values("post_type__name", "subject__name")
        .annotate(
            sanctioned_posts=Sum("total_posts"),
        )
    )

    sanctioned_map = {
        (row["post_type__name"], row["subject__name"]): row["sanctioned_posts"]
        for row in sanctioned
    }

    # 2. Fetch working staff
    staff_summary = (
        Staff.objects.filter(school=school, post_type__name__in=allowed_post_types)
        .values("post_type__name", "subject__name")
        .annotate(
            regular_working=Count("id", filter=Q(employment_type="Regular")),
            guest_working=Count("id", filter=Q(employment_type="Guest")),
            hkrnl_working=Count("id", filter=Q(employment_type="HKRNL")),
            male_working=Count("id", filter=Q(gender="Male")),
            female_working=Count("id", filter=Q(gender="Female")),
        )
    )

    staff_map = {
        (row["post_type__name"], row["subject__name"]): row
        for row in staff_summary
    }

    # 3. Merge (loop only over sanctioned posts)
    merged = []
    for key, sanctioned_posts in sanctioned_map.items():
        post_type, subject = key
        staff_data = staff_map.get(key, {})

        row = {
            "post_type__name": post_type,
            "subject__name": subject,
            "sanctioned_posts": sanctioned_posts,
            "regular_working": staff_data.get("regular_working", 0),
            "guest_working": staff_data.get("guest_working", 0),
            "hkrnl_working": staff_data.get("hkrnl_working", 0),
            "male_working": staff_data.get("male_working", 0),
            "female_working": staff_data.get("female_working", 0),
        }

        row["vacant"] = sanctioned_posts - row["regular_working"]
        row["net_vacancy"] = (
            sanctioned_posts
            - row["regular_working"]
            - row["guest_working"]
            - row["hkrnl_working"]
        )

        merged.append(row)

    # 4. Sort according to required order
    post_order = {name: i for i, name in enumerate(allowed_post_types)}
    merged.sort(key=lambda x: post_order.get(x["post_type__name"], 999))

    return render(request, "staff_summary.html", {"summary": merged, "school": school})


def achievement_list(request):
    achievements = StudentAchievement.objects.select_related("exam_detail").all().order_by("-date")
    return render(request, "achievement_list.html", {"achievements": achievements})

def achievement_detail(request, pk):
    achievement = get_object_or_404(StudentAchievement.objects.select_related("exam_detail"), pk=pk)
    return render(request, "achievement_detail.html", {"achievement": achievement})

def signin_link(request):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # ✅ distinct combinations of class and section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # ✅ Define custom order for classes
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # ✅ Sort by studentclass (custom order) then section (alphabetically)
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(
        request,
        "signin_link.html",
        {
            "class_sections": class_sections,
            "school": school  # ✅ also send school to template
        }
    )


from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import datetime

def signin(request, class_name, section_name):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)  # optional logo

    # Filter students
    # Filter students and sort by roll_number
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="attendance_{class_name}_{section_name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    # Custom styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    heading_style = ParagraphStyle(name="Heading", fontSize=14, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header: Logo + School Name + Address ---
    header_table_data = []

    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10)
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info Box ---
    class_info = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200]
    )
    class_info.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(class_info)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [["SRN", "Roll No", "Student's Name", "Sub 1", "Sub 2", "Sub 3", "Sub 4", "Sub 5", "Sub 6", "Sub 7"]]

    # --- Student rows ---
    for idx, student in enumerate(students, start=1):
        data.append([
            student.srn,
            student.roll_number,
            student.full_name_aadhar,
            "", "", "", "", "", "", ""
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[60, 50, 200, 60, 60, 60, 60, 60, 60, 60])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor('#AED6F1')),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (1,-1), "CENTER"),
        ("ALIGN", (2,0), (2,-1), "LEFT"),
        ("ALIGN", (3,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # Alternate row background
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # --- Footer with signature lines ---
    footer_data = [
        ["Class Teacher Signature: ______________________", "", "Principal Signature: ______________________"]
    ]
    footer_table = Table(footer_data, colWidths=[250, 100, 250])
    footer_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 20)
    ]))
    elements.append(footer_table)

    # --- Page number function ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response


from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import datetime

def roll_call_link(request):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # ✅ distinct combinations of class and section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # ✅ Define custom order for classes
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # ✅ Sort by studentclass (custom order) then section (alphabetically)
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(request, "roll_call_link.html", {"class_sections": class_sections, "school": school})


def roll_call(request, class_name, section_name):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)

    # Filter students
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="roll_call_register_{class_name}_{section_name}.pdf"'

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20,
    )
    elements = []
    styles = getSampleStyleSheet()

    # Custom styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header: Logo + School Name ---
    header_table_data = []
    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info ---
    class_info = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200],
    )
    class_info.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(class_info)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [[
        "SRN", "Roll No", "Adm No", "Student's Name",
        "DOB", "Gender", "Aadhaar No",
        "Father's Name", "Mother's Name", "Mobile No.", "Category"
    ]]

    # --- Student Rows ---
    for student in students:
        data.append([
            student.srn,
            student.roll_number,
            student.admission_number,
            student.full_name_aadhar,
            student.date_of_birth.strftime("%d-%m-%Y") if student.date_of_birth else "",
            student.gender,
            student.aadhaar_number,
            student.father_full_name_aadhar,
            student.mother_full_name_aadhar,
            student.father_mobile,
            student.category,
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[50, 30, 40, 100, 70, 50, 80, 100, 100, 80, 70])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (2,-1), "CENTER"),
        ("ALIGN", (4,0), (4,-1), "LEFT"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # Alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)

    # --- Page numbers ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response


from collections import defaultdict
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

from collections import defaultdict
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

def generate_student_strength_pdf(request):
    # -------------------------------------------------
    # 🔹 Mapping of DB values -> Display
    # -------------------------------------------------
    class_mapping = {
        "sixth": "6th",
        "seventh": "7th",
        "eighth": "8th",
        "nineth": "9th",
        "ninth": "9th",   # ✅ handle both spellings
        "tenth": "10th",
        "eleventh": "11th",
        "twelfth": "12th",
    }

    # Natural order for sorting
    class_order = {
        c: i for i, c in enumerate(
            ["sixth", "seventh", "eighth", "nineth", "ninth", "tenth", "eleventh", "twelfth"]
        )
    }

    category_list = ["SC", "BC-A", "BC-B", "GEN"]

    # -------------------------------------------------
    # 📊 Group students by class-section
    # -------------------------------------------------
    section_data = defaultdict(lambda: [0] * 8)  # [SC_M, SC_F, BCA_M, BCA_F, BCB_M, BCB_F, GEN_M, GEN_F]

    students = Student.objects.exclude(studentclass__isnull=True).exclude(section__isnull=True)

    for student in students:
        cls = (student.studentclass or "").strip().lower()
        sec = (student.section or "NA").strip().upper()
        gender = (student.gender or "").strip().lower()
        category = (student.category or "").strip().upper()

        if cls not in class_mapping:
            continue  # skip classes outside 6th–12th

        if category not in category_list:
            category = "GEN"  # fallback if unknown

        base_index = category_list.index(category) * 2
        if gender == "male":
            section_data[(cls, sec)][base_index] += 1
        elif gender == "female":
            section_data[(cls, sec)][base_index + 1] += 1
        else:
            section_data[(cls, sec)][base_index] += 1  # default to male col

    # -------------------------------------------------
    # 🏷️ Helper to build table data (class-wise sorting)
    # -------------------------------------------------
    def build_table_data(classes_subset):
        # Header rows
        data = [
            ["Class", "Section",
             "SC", "", "", "BCA", "", "", "BCB", "", "", "GEN", "", "", "Grand Total"],
            ["", "", "Male", "Female", "Total",
             "Male", "Female", "Total",
             "Male", "Female", "Total",
             "Male", "Female", "Total",
             "Total"],
        ]

        block_total = [0] * 8

        # ✅ loop classes in correct order
        for cls in sorted(classes_subset, key=lambda c: class_order.get(c, 999)):
            class_total = [0] * 8

            # all sections for this class
            for (cur_cls, sec), counts in sorted(
                section_data.items(),
                key=lambda x: x[0][1]  # sort sections alphabetically
            ):
                if cur_cls != cls:
                    continue

                sc_total = counts[0] + counts[1]
                bca_total = counts[2] + counts[3]
                bcb_total = counts[4] + counts[5]
                gen_total = counts[6] + counts[7]
                grand_total = sc_total + bca_total + bcb_total + gen_total

                data.append([
                    class_mapping.get(cur_cls, cur_cls), sec,
                    counts[0], counts[1], sc_total,
                    counts[2], counts[3], bca_total,
                    counts[4], counts[5], bcb_total,
                    counts[6], counts[7], gen_total,
                    grand_total
                ])

                # accumulate into class total
                class_total = [a+b for a, b in zip(class_total, counts)]

            # ✅ add total row for this class
            if sum(class_total) > 0:
                sc_total = class_total[0] + class_total[1]
                bca_total = class_total[2] + class_total[3]
                bcb_total = class_total[4] + class_total[5]
                gen_total = class_total[6] + class_total[7]
                grand_total = sc_total + bca_total + bcb_total + gen_total

                data.append([
                    f"Total {class_mapping.get(cls, cls)}", "",
                    class_total[0], class_total[1], sc_total,
                    class_total[2], class_total[3], bca_total,
                    class_total[4], class_total[5], bcb_total,
                    class_total[6], class_total[7], gen_total,
                    grand_total
                ])

                # add into block total
                block_total = [a+b for a, b in zip(block_total, class_total)]

        # ✅ finally block total
        sc_total = block_total[0] + block_total[1]
        bca_total = block_total[2] + block_total[3]
        bcb_total = block_total[4] + block_total[5]
        gen_total = block_total[6] + block_total[7]
        grand_total = sc_total + bca_total + bcb_total + gen_total

        data.append([
            f"Total ({', '.join(class_mapping[c] for c in classes_subset if c in class_mapping)})", "",
            block_total[0], block_total[1], sc_total,
            block_total[2], block_total[3], bca_total,
            block_total[4], block_total[5], bcb_total,
            block_total[6], block_total[7], gen_total,
            grand_total
        ])

        return data, block_total

    # -------------------------------------------------
    # 📌 Prepare PDF
    # -------------------------------------------------
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="student_strength.pdf"'

    page_width, page_height = landscape(A4)
    doc = SimpleDocTemplate(
        response,
        pagesize=(page_width, page_height),
        leftMargin=20, rightMargin=20,
        topMargin=20, bottomMargin=20
    )

    elements = []
    styles = getSampleStyleSheet()

    # -------------------------------------------------
    # Page 1 → 6th to 8th
    # -------------------------------------------------
    elements.append(Paragraph("<b>Student Strength Report (6th to 8th)</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    data_6_8, total_6_8 = build_table_data(["sixth", "seventh", "eighth"])
    col_widths = [50, 50] + [40] * (len(data_6_8[0]) - 2)

    table1 = Table(data_6_8, colWidths=col_widths, repeatRows=2)
    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("BACKGROUND", (0, 1), (-1, 1), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 1), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

        # spans
        ("SPAN", (0, 0), (0, 1)),  # Class
        ("SPAN", (1, 0), (1, 1)),  # Section
        ("SPAN", (2, 0), (4, 0)),  # SC
        ("SPAN", (5, 0), (7, 0)),  # BCA
        ("SPAN", (8, 0), (10, 0)), # BCB
        ("SPAN", (11, 0), (13, 0)),# GEN
        ("SPAN", (14, 0), (14, 1)),# Grand Total

        ("BACKGROUND", (0, -1), (-1, -1), colors.lightgrey),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
    ])
    table1.setStyle(style)
    elements.append(table1)

    elements.append(PageBreak())

    # -------------------------------------------------
    # Page 2 → 9th to 12th
    # -------------------------------------------------
    elements.append(Paragraph("<b>Student Strength Report (9th to 12th)</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    data_9_12, total_9_12 = build_table_data(["ninth", "nineth", "tenth", "eleventh", "twelfth"])
    table2 = Table(data_9_12, colWidths=col_widths, repeatRows=2)
    table2.setStyle(style)
    elements.append(table2)

    # -------------------------------------------------
    # Optional Grand Total across 6th–12th
    # -------------------------------------------------
    grand_total = [a+b for a, b in zip(total_6_8, total_9_12)]
    sc_total = grand_total[0] + grand_total[1]
    bca_total = grand_total[2] + grand_total[3]
    bcb_total = grand_total[4] + grand_total[5]
    gen_total = grand_total[6] + grand_total[7]
    all_total = sc_total + bca_total + bcb_total + gen_total

    data_grand = [[
        "Grand Total (6th–12th)", "",
        grand_total[0], grand_total[1], sc_total,
        grand_total[2], grand_total[3], bca_total,
        grand_total[4], grand_total[5], bcb_total,
        grand_total[6], grand_total[7], gen_total,
        all_total
    ]]

    table3 = Table(data_grand, colWidths=col_widths)
    table3.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    elements.append(Spacer(1, 12))
    elements.append(table3)

    # -------------------------------------------------
    # Build PDF
    # -------------------------------------------------
    doc.build(elements)
    return response


def mandatory_public_disclosure(request):
    disclosures = MandatoryPublicDisclosure.objects.filter(is_active=True).order_by("id")

    return render(request, "mandatory_disclosure.html", {"disclosures": disclosures})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index after successful login
        else:
            error = "Invalid username or password"
            return render(request, 'login.html', {'error': error})

    # If GET request, show login page
    return render(request, 'login.html')


# ✅ Show available class-section links
def subject_report_link(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # distinct class-section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # custom order
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # sort by class (custom) then section
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(request, "subject_report_link.html", {
        "class_sections": class_sections,
        "school": school
    })


# ✅ Generate subject report PDF
def subject_report(request, class_name, section_name):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)

    # fetch students
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # response PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="subject_report_{class_name}_{section_name}.pdf"'

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20,
    )

    elements = []
    styles = getSampleStyleSheet()

    # styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header ---
    header_table_data = []
    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info ---
    class_info = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200],
    )
    class_info.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(class_info)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [[
        "SRN", "Roll No",
        "Student's Name", "Subjects"
    ]]

    # --- Student Rows ---
    for student in students:
        data.append([
            student.srn,
            student.roll_number,
            student.full_name_aadhar,
            student.subjects if student.subjects else ""
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[60, 50, 150, 400])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#F9E79F")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (3,-1), "CENTER"),
         ("ALIGN", (2,0), (2,-1), "LEFT"),     # Student's Name left-aligned
        ("ALIGN", (4,0), (5,-1), "LEFT"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)

    # --- Page numbers ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response

def bank_report_link(request):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # ✅ distinct combinations of class and section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # ✅ Define custom order for classes
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # ✅ Sort by studentclass (custom order) then section (alphabetically)
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(request, "bank_report_link.html", {"class_sections": class_sections, "school": school})


def bank_report(request, class_name, section_name):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, "address", "")
    school_logo = getattr(school, "logo", None)

    # ✅ Filter students
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # ✅ PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="bank_report_{class_name}_{section_name}.pdf"'

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20,
    )
    elements = []
    styles = getSampleStyleSheet()

    # ✅ Custom styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header: Logo + School Name ---
    header_table_data = []
    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info ---
    class_info = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200],
    )
    class_info.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(class_info)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [[
        "SRN", "Roll No", "Student's Name",
        "Aadhaar No", "Bank Name","Account Number", "IFSC", "Family ID","Category"
    ]]

    # --- Student Rows ---
    for student in students:
        data.append([
            student.srn,
            
            student.roll_number,
            student.full_name_aadhar,
            student.aadhaar_number,
            
            student.bank_name,
            
            student.account_number,
            student.ifsc,
            student.family_id,
            student.category,
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[50, 40, 100, 90, 240, 80, 70, 60,40])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#F9E79F")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (3,-1), "CENTER"),
        ("ALIGN", (2,0), (2,-1), "LEFT"),
        ("ALIGN", (4,0), (-1,-1), "LEFT"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # Alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)

    # --- Page numbers ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response



def cwsn_students_report(request):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")


    CLASS_ORDER = {
        "Sixth": 6,
        "Seventh": 7,
        "Eighth": 8,
        "Nineth": 9,
        "Tenth": 10,
        "Eleventh": 11,
        "Twelfth": 12,
    }

    students = list(Student.objects.filter(
        school_name=school.name
    ).exclude(disability__isnull=True).exclude(disability__exact=""))

    students.sort(
        key=lambda s: (
            CLASS_ORDER.get(s.studentclass, 99),
            s.section or "",
            s.roll_number or 0
        )
    )
    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="cwsn_students_{school.name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(name="Title", fontSize=16, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    elements.append(Paragraph(f"CWSN Students Report - {school.name}", title_style))
    elements.append(Spacer(1, 12))

    # Table Header
    data = [[
        "SRN", "Class", "Section", "Roll No", "Adm No", "Student's Name",
        "Father's Name", "DOB", "Gender", "Disability"
    ]]

    # Rows
    for s in students:
        data.append([
            s.srn,
            s.studentclass,
            s.section,
            s.roll_number,
            s.admission_number,
            s.full_name_aadhar,
            s.father_full_name_aadhar,
            s.date_of_birth.strftime("%d-%m-%Y") if s.date_of_birth else "",
            s.gender,
            s.disability,
        ])


    # Table
    table = Table(data, repeatRows=1, colWidths=[60, 50, 50, 40, 60, 100, 100, 70, 50, 150])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(table)

    doc.build(elements)
    return response


def bpl_students_report(request):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")


    CLASS_ORDER = {
        "Sixth": 6,
        "Seventh": 7,
        "Eighth": 8,
        "Nineth": 9,
        "Tenth": 10,
        "Eleventh": 11,
        "Twelfth": 12,
    }

    students = list(Student.objects.filter(
        school_name=school.name
    ).exclude(below_poverty_line_certificate_number__isnull=True).exclude(below_poverty_line_certificate_number__exact=""))

    students.sort(
        key=lambda s: (
            CLASS_ORDER.get(s.studentclass, 99),
            s.section or "",
            s.roll_number or 0
        )
    )


    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="bpl_students_{school.name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(name="Title", fontSize=16, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    elements.append(Paragraph(f"BPL Students Report - {school.name}", title_style))
    elements.append(Spacer(1, 12))

    # Table Header
    data = [[
        "SRN", "Class", "Section", "Roll No", "Student's Name",
        "DOB", "Gender", "Account No.", "Family ID","BPL Certificate No.","Category",
    ]]

    # Rows
    for s in students:
        data.append([
            s.srn,
            s.studentclass,
            s.section,
            s.roll_number,
            s.full_name_aadhar,
            s.date_of_birth.strftime("%d-%m-%Y") if s.date_of_birth else "",
            s.gender,
            s.account_number,
            s.family_id,
            s.below_poverty_line_certificate_number,
            s.category,
        ])

    # Table
    table = Table(data, repeatRows=1, colWidths=[60, 50, 50, 40, 100, 70, 50, 90, 60,80,50])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(table)

    doc.build(elements)
    return response

def subjects_offered(request):
    # Ensure a school is selected
    school = get_current_school(request)
    if not school:
        return redirect("select_school")

    # Fetch all ClassSubject for this school
    class_subjects = (
        ClassSubject.objects
        .select_related("class_info__stream", "class_info__medium", "subject")
        .filter(class_info__school=school)
        .order_by("class_info__name", "subject__name")
    )

    # Helper: determine school level
    def get_level(class_name: str):
        try:
            num = int("".join([c for c in class_name if c.isdigit()]))
        except ValueError:
            return "Other"
        if 1 <= num <= 5:
            return "Primary"
        elif 6 <= num <= 8:
            return "Middle"
        elif 9 <= num <= 10:
            return "Secondary"
        elif 11 <= num <= 12:
            return "Senior Secondary"
        return "Other"

    # Initialize grouped_data including 'Other' to avoid KeyError
    grouped_data = {
        "Primary": {},
        "Middle": {},
        "Secondary": {},
        "Senior Secondary": {},
        "Other": {}
    }

    # Organize subjects into level → class → subjects
    for cs in class_subjects:
        level = get_level(cs.class_info.name)
        class_label = cs.class_info.full_display()  # includes stream + medium

        # Safely create entries
        grouped_data.setdefault(level, {})
        grouped_data[level].setdefault(class_label, [])

        grouped_data[level][class_label].append({
            "name": cs.subject.name,
            "periods_per_week": cs.periods_per_week,
            "is_optional": cs.is_optional,
            "has_lab": cs.has_lab,
        })

    return render(
        request,
        "subjects_offered.html",
        {"school": school, "grouped_data": grouped_data},
    )

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

    sections_qs = Section.objects.select_related("school_class").all().order_by("school_class__class_order", "name")
    sections = {sec.id: sec for sec in sections_qs}

    class_subjects_qs = ClassSubject.objects.select_related("class_info", "subject").all()
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
    return render(request, "teacher_subject_section_assignment.html", context)


# AJAX view for filtering subjects by section
def get_subjects_for_section(request):
    section_id = request.GET.get('section_id')
    subjects = []

    if section_id:
        try:
            section = Section.objects.select_related("school_class__stream").get(id=section_id)
            class_subjects = ClassSubject.objects.filter(class_info=section.school_class)
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

    return render(request, "timetable_list.html", {
        "grouped_timetables": grouped_timetables,
        "periods": periods,
        "days": days,
    })




def reports_dashboard(request):
    # Fetch all sections and teachers for dropdowns
    sections = Section.objects.select_related("school_class").order_by("school_class__name", "name")
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

    return render(request, "reports/dashboard.html", context)


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
        "teacher_assignment__section__school_class",
        "slot",
        "classroom"
    ).order_by("slot__day__sequence", "slot__period_number")

    timetable = defaultdict(list)
    for e in entries:
        timetable[e.slot.day.name].append({
            "period": e.slot.period_number,
            "subject": e.teacher_assignment.class_subject.subject.name,
            "teacher": e.teacher_assignment.teacher.name,
            "class_name": e.teacher_assignment.section.school_class.name,
            "section_name": e.teacher_assignment.section.name,
            "classroom": e.classroom.name if e.classroom else None,
        })
    return dict(timetable)


def teacher_timetable_report(teacher_id):
    entries = (
        Timetable.objects.filter(teacher_assignment__teacher_id=teacher_id)
        .select_related(
            "teacher_assignment__section",
            "teacher_assignment__section__school_class",
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
            "class_name": e.teacher_assignment.section.school_class.name,
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
            "teacher_assignment__section__school_class__name",
            "teacher_assignment__section__name",
            "teacher_assignment__class_subject__subject__name"
        )
        .annotate(periods_assigned=Count("id"))
        .order_by(
            "teacher_assignment__section__school_class__name",
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

    # school_name = school.name    



    # school = request.GET.get("school")
    # school = get_object_or_404(School, id=school)

    # Multi-section selection
    section_ids = request.GET.getlist("sections")
    if section_ids:
        sections = Section.objects.filter(id__in=section_ids)
    else:
        sections = Section.objects.filter(school_class__school=school)

    # Teacher-Subject assignments for selected sections
    assignments = (
        TeacherSubjectAssignment.objects.filter(section__in=sections)
        .select_related(
            "teacher",
            "class_subject__subject",
            "section__school_class",
            "section__classroom"
        )
    )

    # Current Timetable entries
    timetable_entries = (
        Timetable.objects.filter(teacher_assignment__section__in=sections)
        .select_related(
            "teacher_assignment__teacher",
            "teacher_assignment__class_subject__subject",
            "slot",
            "classroom",
            "teacher_assignment__section__school_class"
        )
    )

    # Build lookup dict: timetable_lookup[day][period][section_id] = entries
    timetable_lookup = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for entry in timetable_entries:
        day_id = entry.slot.day.id
        period = entry.slot.period_number or 0
        timetable_lookup[day_id][period][entry.section.id].append(entry)

    # Period numbers
    period_numbers = list(
        TimetableSlot.objects.filter(school=school)
        .values_list("period_number", flat=True)
        .distinct()
        .order_by("period_number")
    )

    # Precompute workloads
    teacher_loads = defaultdict(int)
    subject_loads = defaultdict(int)

    # Teacher load across all sections (global)
    all_teachers = [a.teacher for a in assignments]
    for entry in Timetable.objects.filter(teacher_assignment__teacher__in=all_teachers):
        teacher_loads[entry.teacher.id] += 1

    # Subject load per section
    for entry in timetable_entries:
        subject_loads[(entry.class_subject.id, entry.section.id)] += 1

    # Add workload info to assignments
    assignment_data = []
    for assign in assignments:
        assignment_data.append({
            "id": assign.id,
            "teacher": assign.teacher,
            "class_subject": assign.class_subject,
            "section": assign.section,
            "current_load": teacher_loads[assign.teacher.id],
            "max_load": assign.teacher.max_periods_per_week,
            "current_subject_load": subject_loads[(assign.class_subject.id, assign.section.id)],
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
            school=tsa.section.school_class.school
        )

        tt_entry, created = Timetable.objects.update_or_create(
            teacher_assignment=tsa,
            slot=slot,
            defaults={
                "classroom": tsa.section.classroom,
                "school": tsa.section.school_class.school
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




