from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q, Case, When,Sum,OuterRef
from django.http import FileResponse, Http404
from .utils import get_current_school
from .models import (
    Staff, Student, Class, Subject,
    News, SMCMember, Committee, School,FeeStructure,FAQ,
    AboutSchool, Principal, Affiliation,StaffAssociationRoleAssignment, Association,StudentAchievement,Infrastructure,SanctionedPost
   
)
from cms.utils import generate_timetable
import itertools
from django.db.models import Prefetch
import os
from django.conf import settings
# -------------------- Utility --------------------




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

def fee_structure(request):
    fee_data = FeeStructure.objects.all().order_by('student_class')
    return render(request, "fee_structure.html", {"fee_data": fee_data})

#def fee_structure(request): return render(request, "fee_structure.html")
def faq(request):
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'category')
    # Optional: group by category
    categories = {}
    for faq in faqs:
        categories.setdefault(faq.get_category_display(), []).append(faq)
    return render(request, 'faq.html', {'categories': categories})
# def faq(request): return render(request, "faq.html")

def mandatory_disclosure(request): return render(request, "mandatory_disclosure.html")
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

