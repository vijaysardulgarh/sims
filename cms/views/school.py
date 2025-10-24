from django.shortcuts import render, get_object_or_404, redirect
from cms.utils import get_current_school
from ..models.school import AboutSchool,Principal,Affiliation,MandatoryPublicDisclosure
from ..models.finance import FeeStructure
from ..models.common import FAQ

def about_school(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    about = AboutSchool.objects.filter(school=school).first()
    return render(request, "about_us/about.html", {"about": about})

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



def infrastructure(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")  # if no school in session, send user back to homepage

    infrastructures = school.infrastructures.all().order_by("category")
    return render(request, "about_us/infrastructure.html", {
        "school": school,
        "infrastructures": infrastructures
    })


def mandatory_public_disclosure(request):
    disclosures = MandatoryPublicDisclosure.objects.filter(is_active=True).order_by("id")

    return render(request, "mandatory_disclosure.html", {"disclosures": disclosures})

def document_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    documents = school.documents.all()
    return render(request, "document_detail.html", {"school": school, "documents": documents})

def infrastructure(request): 
    return render(request, "about_us/infrastructure.html")


def faq(request):
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'category')
    # Optional: group by category
    categories = {}
    for faq in faqs:
        categories.setdefault(faq.get_category_display(), []).append(faq)
    return render(request, 'faq.html', {'categories': categories})

def achievements(request): 
    return render(request, "achievements.html")

def board_results(request): 
    return render(request, "board_results.html")

def sports_achievements(request): 
    return render(request, "sports.html")

def contact(request):
    school = get_current_school(request)
    return render(request, "contact.html", {"school": school})

def fee_structure_list(request):
    fee_structures = FeeStructure.objects.select_related("student_class", "stream", "student_class__school")
    return render(request, "fees_list.html", {"fee_structures": fee_structures})