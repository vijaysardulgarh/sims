# context_processors.py
from .models import Association
from .utils import get_current_school


def committees_context(request):
    school = get_current_school(request)
    committees = []
    if school:
        committees = Association.objects.filter(
            school=school,
            type__name="Committee"
        ).order_by("name")
    return {"menu_committees": committees}

