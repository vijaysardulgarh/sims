from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.exams.models import ExamType
from apps.exams.serializers import ExamTypeSerializer


# =====================================
# EXAM TYPE LIST / CREATE
# =====================================

class ExamTypeListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = ExamType.objects.all().order_by(
        "name"
    )

    serializer_class = ExamTypeSerializer

    permission_classes = [
        IsAuthenticated
    ]


# =====================================
# EXAM TYPE DETAIL
# =====================================

class ExamTypeDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = ExamType.objects.all()

    serializer_class = ExamTypeSerializer

    permission_classes = [
        IsAuthenticated
    ]