from django.shortcuts import render

from django.db.models import (
    Count,
    Q,
    Case,
    When
)

from collections import defaultdict

from apps.students.models import (
    Student
)

from apps.academics.models import (
    ClassSubject,
    Timetable
)


# =========================================
# SUBJECT STRENGTH REPORT
# =========================================

def subject_strength_view(request):

    class_order = {
        "Sixth": 1,
        "Seventh": 2,
        "Eighth": 3,
        "Nineth": 4,
        "Tenth": 5,
        "Eleventh": 6,
        "Twelfth": 7,
    }

    data = list(

        Student.objects

        .values(
            "studentclass",
            "section",
            "stream"
        )

        .annotate(

            english=Count(
                "srn",
                filter=Q(
                    subjects_opted__icontains="English"
                )
            ),

            mathematics=Count(
                "srn",
                filter=Q(
                    subjects_opted__icontains="Mathematics"
                )
            ),

            science=Count(
                "srn",
                filter=Q(
                    subjects_opted__icontains="Science"
                )
            ),

            physics=Count(
                "srn",
                filter=Q(
                    subjects_opted__icontains="Physics"
                )
            ),

            chemistry=Count(
                "srn",
                filter=Q(
                    subjects_opted__icontains="Chemistry"
                )
            ),

            biology=Count(
                "srn",
                filter=Q(
                    subjects_opted__icontains="Biology"
                )
            ),

            order=Case(
                *[
                    When(
                        studentclass=cls,
                        then=pos
                    )
                    for cls, pos in class_order.items()
                ]
            )
        )

        .order_by("order")
    )

    return render(
        request,
        "academics/reports/subject_strength.html",
        {
            "data": data
        }
    )


# =========================================
# SUBJECTS OFFERED REPORT
# =========================================

def subjects_offered_view(request):

    class_subjects = (

        ClassSubject.objects

        .select_related(
            "class_obj",
            "stream",
            "subject"
        )

        .order_by(
            "class_obj__name",
            "subject__name"
        )
    )

    grouped_data = defaultdict(list)

    for cs in class_subjects:

        class_name = cs.class_obj.name

        if cs.stream:
            class_name += f" - {cs.stream.name}"

        if cs.sub_stream:
            class_name += f" - {cs.sub_stream}"

        grouped_data[class_name].append({

            "subject":
                cs.subject.name,

            "periods_per_week":
                cs.periods_per_week,

            "is_optional":
                cs.is_optional,

            "has_lab":
                cs.has_lab,
        })

    return render(
        request,
        "academics/reports/subjects_offered.html",
        {
            "grouped_data": dict(grouped_data)
        }
    )


# =========================================
# TEACHER WORKLOAD REPORT
# =========================================

def teacher_workload_view(request):

    data = (

        Timetable.objects

        .values(
            "teacher_subject_assignment__teacher__name"
        )

        .annotate(
            total=Count("id")
        )
    )

    return render(
        request,
        "academics/reports/teacher_workload.html",
        {
            "data": data
        }
    )