from rest_framework.views import APIView
from rest_framework.response import Response

from collections import defaultdict

from apps.timetables.class_subjects.models import (
    ClassSubject
)


class SubjectsOfferedAPIView(APIView):

    def get(self, request):

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

        return Response(grouped_data)