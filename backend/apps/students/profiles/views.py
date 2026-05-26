from rest_framework import generics

from apps.students.profiles.models import Student

from apps.students.profiles.serializers import (
    StudentSerializer
)


# =========================================
# STUDENT LIST CREATE API
# =========================================

class StudentListCreateAPIView(

    generics.ListCreateAPIView
):

    queryset = (
        Student.objects.all()
        .order_by("-srn")
    )

    serializer_class = (
        StudentSerializer
    )

    def perform_create(
        self,
        serializer
    ):

        school = getattr(
            self.request.user,
            "school",
            None
        )

        if not school:

            from apps.schools.models import (
                School
            )

            school = (
                School.objects.first()
            )

        serializer.save(
            school=school
        )


# =========================================
# STUDENT DETAIL API
# =========================================

class StudentRetrieveUpdateDestroyAPIView(

    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Student.objects.all()

    serializer_class = (
        StudentSerializer
    )

    lookup_field = "srn"