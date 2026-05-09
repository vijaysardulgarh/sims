from apps.schools.models import School


def get_current_school(request):

    school_id = request.GET.get("school_id")

    if not school_id:
        return None

    try:
        return School.objects.get(id=school_id)

    except School.DoesNotExist:
        return None