from django import template
from django.db.models import Count, Q
from cms.models import Student, Staff, News, SMCMember, Committee
import hashlib
register = template.Library()

# =====================
# Student Stats Filters
# =====================

@register.simple_tag
def get_lower_class_stats(school_name):
    lower_classes = ['Sixth', 'Seventh', 'Eighth']
    return Student.objects.filter(
        school_name=school_name,
        studentclass__in=lower_classes
    ).aggregate(
        scmale=Count('srn', filter=Q(gender='Male', category__in=['SC', 'Scheduled Caste'])),
        scfemale=Count('srn', filter=Q(gender='Female', category__in=['SC', 'Scheduled Caste'])),
        bcamale=Count('srn', filter=Q(gender='Male', category='BC-A')),
        bcafemale=Count('srn', filter=Q(gender='Female', category='BC-A')),
        bcbmale=Count('srn', filter=Q(gender='Male', category='BC-B')),
        bcbfemale=Count('srn', filter=Q(gender='Female', category='BC-B')),
        genmale=Count('srn', filter=Q(gender='Male', category__in=['GEN', 'General'])),
        genfemale=Count('srn', filter=Q(gender='Female', category__in=['GEN', 'General'])),
    )

@register.simple_tag
def get_upper_class_stats(school_name):
    upper_classes = ['Nineth', 'Tenth', 'Eleventh', 'Twelfth']
    return Student.objects.filter(
        school_name=school_name,
        studentclass__in=upper_classes
    ).aggregate(
        scmale=Count('srn', filter=Q(gender='Male', category__in=['SC', 'Scheduled Caste'])),
        scfemale=Count('srn', filter=Q(gender='Female', category__in=['SC', 'Scheduled Caste'])),
        bcamale=Count('srn', filter=Q(gender='Male', category='BC-A')),
        bcafemale=Count('srn', filter=Q(gender='Female', category='BC-A')),
        bcbmale=Count('srn', filter=Q(gender='Male', category='BC-B')),
        bcbfemale=Count('srn', filter=Q(gender='Female', category='BC-B')),
        genmale=Count('srn', filter=Q(gender='Male', category__in=['GEN', 'General'])),
        genfemale=Count('srn', filter=Q(gender='Female', category__in=['GEN', 'General'])),
    )

# =====================
# Staff & News Queries
# =====================

@register.simple_tag
def get_teaching_staff():
    return Staff.objects.filter(staff_role='Teaching').order_by('post_type', 'name')

@register.simple_tag
def get_non_teaching_staff():
    return Staff.objects.filter(staff_role='Non-Teaching').order_by('post_type', 'name')

@register.simple_tag
def get_academic_news(limit=10):
    return News.objects.filter(category__iexact='Academics')[:limit]

@register.simple_tag
def get_event_news(limit=10):
    return News.objects.filter(category__iexact='Events')[:limit]

# =====================
# Committees & SMC
# =====================

@register.simple_tag
def get_smc_members():
    return SMCMember.objects.all()

@register.simple_tag
def get_committees():
    return Committee.objects.all()

@register.inclusion_tag("partials/sidebar.html", takes_context=True)
def show_sidebar(context):
    school_name = "PM Shri Government Senior Secondary School Nagpur"

    return {
        "stats_lower": get_lower_class_stats(school_name),
        "stats_upper": get_upper_class_stats(school_name),
        "teaching_staff": get_teaching_staff(),
        "non_teaching_staff": get_non_teaching_staff(),
        "academic_news": get_academic_news(10),
        "event_news": get_event_news(10),
        "smcmembers": get_smc_members(),
        "committees": get_committees(),
    }


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def dict_items(value):
    """Return items() of a dictionary for template iteration."""
    if isinstance(value, dict):
        return value.items()
    return []

@register.filter
def to_range(start, end):
    """
    Usage: 1|to_range:7  → gives [1,2,3,4,5,6,7]
    """
    return range(start, end + 1)

@register.filter
def split(value, delimiter=","):
    return value.split(delimiter)

@register.filter
def groupby_attr(value, attr_name):
    """
    Groups a queryset/list of objects by a given attribute name.
    Usage: {% for day, items in timetables|groupby_attr:"slot.day" %}
    """
    # Sort by attribute first
    sorted_list = sorted(value, key=lambda x: getattr_nested(x, attr_name))
    # Group by attribute
    return [(k, list(g)) for k, g in groupby(sorted_list, key=lambda x: getattr_nested(x, attr_name))]

def getattr_nested(obj, attr):
    """Supports nested attributes like 'slot.day.name'"""
    for part in attr.split("."):
        obj = getattr(obj, part)
    return obj

@register.filter
def get_slot(slots, day_period):
    """
    day_period: "Monday-1"
    slots: queryset of TimetableSlot
    """
    try:
        day_name, period_number = day_period.split("-")
        period_number = int(period_number)
        return slots.filter(day__name=day_name, period_number=period_number).first()
    except Exception:
        return None
    

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, [])


@register.filter
def get_item(dictionary, key):
    """Get value from dictionary safely."""
    if dictionary is None:
        return None
    return dictionary.get(key)

@register.filter
def dict_get(d, key):
    return d.get(key, None)


@register.filter
def get_item(dictionary, key):
    """
    Returns the value for the given key in a dictionary.
    Supports nested keys if passed as tuple.
    """
    if dictionary is None:
        return None

    # Support tuple key
    if isinstance(key, tuple) or isinstance(key, list):
        result = dictionary
        try:
            for k in key:
                result = result.get(k, {})
            return result
        except AttributeError:
            return None
    return dictionary.get(key)

@register.filter
def color_hash(value):
    """
    Generates a consistent pastel background color for a string (like a subject name).
    """
    h = hashlib.md5(value.encode()).hexdigest()
    r = int(h[:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    # Lighten color
    r = (r + 128) // 2
    g = (g + 128) // 2
    b = (b + 128) // 2
    return f"rgb({r},{g},{b})"
