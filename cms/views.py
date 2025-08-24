from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q, Case, When
from .utils import get_current_school
from .models import (
    Staff, Student, Class, Subject, TimeSlot,
    News, SMCMember, Committee, School,
    AboutSchool, Principal, Affiliation,StaffAssociationRoleAssignment, Association,Infrastructure,SanctionedPost
   
)
from cms.utils import generate_timetable
import itertools
from django.db.models import Prefetch

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
    return render(request, "about.html", {"about": about})


def smc_members(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    smcmembers = SMCMember.objects.filter(school=school)
    return render(request, "smc_members.html", {"smcmembers": smcmembers})


def principal(request):
    school = get_current_school(request)
    message = Principal.objects.filter(school=school).first() if school else Principal.objects.first()
    return render(request, "principal.html", {"message": message})


def affiliation_status(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    affiliations = Affiliation.objects.filter(school=school)
    return render(request, "affiliation_status.html", {"school": school, "affiliations": affiliations})


# -------------------- Static Pages --------------------

def management(request): return render(request, "management.html")
def committee(request): return render(request, "committee.html")
def infrastructure(request): return render(request, "infrastructure.html")

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
def admission_form(request): return render(request, "admission_form.html")
def prospectus(request): return render(request, "prospectus.html")
def fee_structure(request): return render(request, "fee_structure.html")
def faq(request): return render(request, "faq.html")

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
        "nodal.html",   # ✅ renamed template
        {"staff_members": staff_members, "school": school},
    )

def infrastructure(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")  # if no school in session, send user back to homepage

    infrastructures = school.infrastructures.all().order_by("category")
    return render(request, "infrastructure.html", {
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
    school = get_current_school(request)

    if not school:
        sanctioned_posts = []
        summary_data = []
    else:
        sanctioned_posts = (
            SanctionedPost.objects.filter(school=school)
            .select_related("subject")
        )

        summary_data = []
        for sp in sanctioned_posts:
            staff_queryset = Staff.objects.filter(school=school)

            # Use subject_id instead of object comparison
            if sp.subject_id:
                staff_queryset = staff_queryset.filter(subject_id=sp.subject_id)

            # Safe total posts
            total_posts = sp.total_posts or 0

            # Case-insensitive filter for employment_type
            regular = staff_queryset.filter(employment_type__iexact="Regular").count()
            guest   = staff_queryset.filter(employment_type__iexact="Guest").count()
            hkrnl   = staff_queryset.filter(employment_type__iexact="HKRNL").count()

            male    = staff_queryset.filter(gender__iexact="Male").count()
            female  = staff_queryset.filter(gender__iexact="Female").count()

            vacant_regular = max(total_posts - regular, 0)
            net_vacancy = max(total_posts - (regular + guest + hkrnl), 0)

            # Debug print (optional: remove later)
            print(f"[DEBUG] {sp.get_post_type_display()} - {sp.designation} ({sp.subject})")
            print("Matched Staff:", list(staff_queryset.values("name", "employment_type", "gender")))

            summary_data.append({
                "post_type": sp.get_post_type_display(),
                "designation": sp.designation or (sp.subject.name if sp.subject else ""),
                "sanction_post": total_posts,
                "regular_working": regular,
                "vacant_regular_only": vacant_regular,
                "guest_working": guest,
                "hkrnl_working": hkrnl,
                "net_vacancy": net_vacancy,
                "male_working": male,
                "female_working": female,
            })

    context = {"summary_data": summary_data, "school": school}
    return render(request, "staff_summary.html", context)

