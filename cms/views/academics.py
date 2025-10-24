
from django.shortcuts import render, get_object_or_404, redirect
from cms.utils import get_current_school
from ..models.student import Student,StudentAchievement
from django.db.models import Count, Q,Case,When
from ..models.subject import ClassSubject
def achievement_list(request):
    achievements = StudentAchievement.objects.select_related("exam_detail").all().order_by("-date")
    return render(request, "achievement_list.html", {"achievements": achievements})

def achievement_detail(request, pk):
    achievement = get_object_or_404(StudentAchievement.objects.select_related("exam_detail"), pk=pk)
    return render(request, "achievement_detail.html", {"achievement": achievement})


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
        science = Count("srn",filter=Q(subjects_opted__iregex=r"\bScience(\s*(and|&)\s*Technology)?\b")),
        # science=Count("srn", filter=Q(subjects_opted__icontains="Science") & ~Q(subjects_opted__icontains="Political Science")& ~Q(subjects_opted__icontains="Computer Science") & ~Q(subjects_opted__icontains="Home Science")),
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



def subjects_offered(request):
    # Ensure a school is selected
    school = get_current_school(request)
    if not school:
        return redirect("select_school")

    # Fetch all ClassSubject for this school
    class_subjects = (
        ClassSubject.objects
        .select_related("subject_class", "stream", "subject")
        .filter(subject_class__school=school)
        .order_by("subject_class__name", "subject__name")
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
        level = get_level(cs.subject_class.name)
        parts = [cs.subject_class.name]
        if cs.stream:
            parts.append(cs.stream.name)
        if cs.sub_stream:
            parts.append(cs.sub_stream)
        class_label = " - ".join(parts)


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


    