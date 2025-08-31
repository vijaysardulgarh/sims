from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q, Case, When,Sum,OuterRef,IntegerField,Value,CharField
from django.http import FileResponse, Http404
from .utils import get_current_school
from .models import (
    Staff, Student, Class, Subject,MandatoryPublicDisclosure,
    News, SMCMember, Committee, School,FeeStructure,FAQ,
    AboutSchool, Principal, Affiliation,StaffAssociationRoleAssignment, Association,StudentAchievement,Infrastructure,SanctionedPost
   
)
from collections import defaultdict
from cms.utils import generate_timetable
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

from reportlab.platypus import Spacer
# -------------------- Dashboard & Common --------------------

def index(request):
    schools = School.objects.all()
    selected_school_id = request.session.get("school_id")
    selected_school = None
    if selected_school_id:
        selected_school = School.objects.filter(id=selected_school_id).first()

    if request.method == "POST":
        school_id = request.POST.get("school")
        if school_id:
            request.session["school_id"] = int(school_id)
            return redirect("/")

    context = {
        "schools": schools,
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
        science=Count("srn", filter=Q(subjects_opted__icontains="Science") & ~Q(subjects_opted__icontains="Political Science") & ~Q(subjects_opted__icontains="Home Science")),
        physics=Count("srn", filter=Q(subjects_opted__icontains="Physics")),
        chemistry=Count("srn", filter=Q(subjects_opted__icontains="Chemistry")),
        biology=Count("srn", filter=Q(subjects_opted__icontains="Biology")),
        home_science=Count("srn", filter=Q(subjects_opted__icontains="Home Science")),
        physical_education=Count("srn", filter=Q(subjects_opted__icontains="Physical and Health Education") | Q(subjects_opted__icontains="Physical Education")),
        automobile=Count("srn", filter=Q(subjects_opted__icontains="Automotive")),
        beauty_wellness=Count("srn", filter=Q(subjects_opted__icontains="Beauty & Wellness")),
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

    # 1. Fetch sanctioned posts for this school
    sanctioned = (
        SanctionedPost.objects.filter(school=school)
        .values("post_type__name", "subject__name")
        .annotate(
            sanctioned_posts=Sum("total_posts"),
        )
    )

    # Convert into dictionary for easy lookup
    sanctioned_map = {
        (row["post_type__name"], row["subject__name"]): row["sanctioned_posts"]
        for row in sanctioned
    }

    # 2. Fetch actual working staff
    summary = (
        Staff.objects.filter(school=school)
        .values("post_type__name", "subject__name")
        .annotate(
            regular_working=Count("id", filter=Q(employment_type="Regular")),
            guest_working=Count("id", filter=Q(employment_type="Guest")),
            hkrnl_working=Count("id", filter=Q(employment_type="HKRNL")),
            male_working=Count("id", filter=Q(gender="Male")),
            female_working=Count("id", filter=Q(gender="Female")),
        )
    )

    # 3. Merge with sanctioned posts
    merged = []
    for row in summary:
        sanctioned_posts = sanctioned_map.get(
            (row["post_type__name"], row["subject__name"]), 0
        )
        row["sanctioned_posts"] = sanctioned_posts
        row["vacant"] = sanctioned_posts - row["regular_working"]
        row["net_vacancy"] = (
            sanctioned_posts
            - row["regular_working"]
            - row["guest_working"]
            - row["hkrnl_working"]
        )
        merged.append(row)

    return render(request, "staff_summary.html", {"summary": merged, "school": school})


def achievement_list(request):
    achievements = StudentAchievement.objects.select_related("exam_detail").all().order_by("-date")
    return render(request, "achievement_list.html", {"achievements": achievements})

def achievement_detail(request, pk):
    achievement = get_object_or_404(StudentAchievement.objects.select_related("exam_detail"), pk=pk)
    return render(request, "achievement_detail.html", {"achievement": achievement})

def signin_link(request):
    # distinct combinations of class and section
    class_sections = (
        Student.objects.values("studentclass", "section")
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

    return render(request, "signin_link.html", {"class_sections": class_sections})

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
    students = Student.objects.filter(studentclass=class_name, section=section_name).order_by('roll_number')

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
    # ✅ distinct combinations of class and section
    class_sections = (
        Student.objects.values("studentclass", "section")
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

    return render(request, "roll_call_link.html", {"class_sections": class_sections})

def roll_call(request, class_name, section_name):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)

    # Filter students
    students = Student.objects.filter(studentclass=class_name, section=section_name).order_by("roll_number")

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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # redirect to dashboard
        else:
            error = "Invalid credentials"
            return render(request, 'index.html', {'error': error})
    return redirect('index')
