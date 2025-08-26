from django import template
from django.db.models import Count, Q
from cms.models import Student, Staff, News, SMCMember, Committee

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

