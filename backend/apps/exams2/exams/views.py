from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.exams.models import Exam
from apps.exams.serializers import ExamSerializer


# =====================================
# EXAM LIST / CREATE
# =====================================

class ExamListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = Exam.objects.all().order_by(
        "-created_at"
    )

    serializer_class = ExamSerializer

    permission_classes = [
        IsAuthenticated
    ]


# =====================================
# EXAM DETAIL
# =====================================

class ExamDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Exam.objects.all()

    serializer_class = ExamSerializer

    permission_classes = [
        IsAuthenticated
    ]