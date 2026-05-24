from collections import (
    defaultdict
)

from apps.academics.curriculum.class_subjects import (
    ClassSubject
)

from apps.academics.reports.common.base_api import (
    BaseReportAPIView
)


class SubjectsOfferedAPIView(
    BaseReportAPIView
):

    def get(self, request):

        school = self.get_school(
            request
        )

        if not school:

            return (
                self.school_error_response()
            )

        class_subjects = (

            ClassSubject.objects

            .select_related(
                "class_obj",
                "stream",
                "subject"
            )

            .filter(
                school=school
            )

            .order_by(
                "class_obj__class_order",
                "subject__name"
            )
        )

        grouped_data = (
            defaultdict(list)
        )

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

            grouped_data[
                class_name
            ].append({

                "subject":
                    cs.subject.name,

                "theory_periods":
                    cs.theory_periods_per_week,

                "practical_periods":
                    cs.practical_periods_per_week,

                "total_periods":
                    cs.periods_per_week,

                "is_optional":
                    cs.is_optional,

                "has_lab":
                    cs.has_lab,

                "is_shared":
                    cs.is_shared,
            })

        return self.success_response(
            grouped_data
        )