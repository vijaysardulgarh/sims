from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from apps.staff.models import (
    Staff
)

from apps.academics.sections import (
    Section
)

from apps.academics.class_subjects import (
    ClassSubject
)

from apps.academics.teacher_subject_assignments import (
    TeacherSubjectAssignment
)

from apps.academics.teacher_subject_assignments.serializer import (
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
            ClassSubject.objects.all()
        )

        assignments = (

            TeacherSubjectAssignment.objects
            .all()
        )

        serializer = (

            TeacherSubjectAssignmentSerializer(
                assignments,
                many=True
            )
        )

        return Response({

            "teachers":
                list(teachers.values()),

            "sections":
                list(sections.values()),

            "subjects":
                list(subjects.values()),

            "assignments":
                serializer.data,
        })