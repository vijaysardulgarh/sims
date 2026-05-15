from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from apps.staff.models import (
    Staff
)

from apps.academics.sections.models import (
    Section
)

from apps.academics.class_subjects.models import (
    ClassSubject
)

from apps.academics.teacher_subject_assignments.models import (
    TeacherSubjectAssignment
)

from apps.academics.teacher_subject_assignments.serializers import (
    TeacherSubjectAssignmentSerializer
)


class TeacherAssignmentAPIView(
    APIView
):

    def get(self, request):

        teachers = (

            Staff.objects.filter(
                staff_role="Teaching"
            )
        )

        sections = (
            Section.objects.all()
        )

        subjects = (

            ClassSubject.objects

            .select_related(
                "subject"
            )
        )

        assignments = (

            TeacherSubjectAssignment.objects

            .select_related(
                "teacher",
                "class_subject__subject",
                "section"
            )
        )

        serializer = (

            TeacherSubjectAssignmentSerializer(
                assignments,
                many=True
            )
        )

        return Response({

            "teachers":
                list(
                    teachers.values(
                        "id",
                        "name"
                    )
                ),

            "sections":
                list(
                    sections.values(
                        "id",
                        "name"
                    )
                ),

            "subjects":
                list(
                    subjects.values(
                        "id",
                        "subject__name"
                    )
                ),

            "assignments":
                serializer.data,
        })