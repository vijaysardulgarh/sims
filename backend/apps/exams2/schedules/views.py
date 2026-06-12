from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.examination.models import ExamSchedule
from apps.exams.serializers import (
    ExamScheduleSerializer
)


# =====================================
# EXAM SCHEDULE LIST / CREATE
# =====================================

class ExamScheduleListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = ExamSchedule.objects.all().order_by(
        "-created_at"
    )

    serializer_class = (
        ExamScheduleSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


# =====================================
# EXAM SCHEDULE DETAIL
# =====================================

class ExamScheduleDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = ExamSchedule.objects.all()

    serializer_class = (
        ExamScheduleSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]