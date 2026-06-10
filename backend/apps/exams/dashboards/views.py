from django.db.models import Count

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.core.views.base_views import (
    BaseAPIView
)

from apps.exams.exams.models import (
    Exam
)

from apps.students.students.models import (
    Student
)

from apps.exams.result_generations.models import (
    ResultGeneration
)


class ExamDashboardAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        *args,
        **kwargs
    ):

        school = self.get_school()

        total_exams = Exam.objects.filter(
            school=school,
            is_deleted=False,
        ).count()

        active_exams = Exam.objects.filter(
            school=school,
            is_deleted=False,
            is_result_published=False,
        ).count()

        completed_exams = Exam.objects.filter(
            school=school,
            is_deleted=False,
            is_result_published=True,
        ).count()

        total_students = Student.objects.filter(
            school=school,
            is_deleted=False,
        ).count()

        published_results = (
            ResultGeneration.objects.filter(
                school=school,
                is_deleted=False,
                is_published=True,
            ).count()
        )

        pending_results = (
            ResultGeneration.objects.filter(
                school=school,
                is_deleted=False,
                is_published=False,
            ).count()
        )

        data = {

            "total_exams":
                total_exams,

            "active_exams":
                active_exams,

            "completed_exams":
                completed_exams,

            "result_published":
                published_results,

            "pending_results":
                pending_results,

            "total_students":
                total_students,

            "pass_percentage":
                0,

            "fail_percentage":
                0,
        }

        return self.success_response(
            data=data
        )