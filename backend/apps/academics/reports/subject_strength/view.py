from django.shortcuts import render

from django.db.models import (
    Count,
    Q,
    Case,
    When
)

from apps.students.models import (
    Student
)


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

                    for cls, pos in (
                        class_order.items()
                    )
                ]
            )
        )

        .order_by("order")
    )

    return render(

        request,

        "academics/reports/"
        "subject_strength.html",

        {
            "data": data
        }
    )
