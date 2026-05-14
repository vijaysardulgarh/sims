from django.shortcuts import render

from collections import defaultdict

from apps.academics.class_subjects import (
    ClassSubject
)


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

        class_name = (
            cs.class_obj.name
        )

        if cs.stream:

            class_name += (
                f" - {cs.stream.name}"
            )

        if cs.sub_stream:

            class_name += (
                f" - {cs.sub_stream}"
            )

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

        "academics/reports/"
        "subjects_offered.html",

        {
            "grouped_data":
                dict(grouped_data)
        }
    )