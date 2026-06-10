from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.exams.models import OnlineExam
from apps.exams.serializers import (
    OnlineExamSerializer
)


# =====================================
# ONLINE EXAM LIST / CREATE
# =====================================

class OnlineExamListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = OnlineExam.objects.all().order_by(
        "-id"
    )

    serializer_class = (
        OnlineExamSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


# =====================================
# ONLINE EXAM DETAIL
# =====================================

class OnlineExamDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = OnlineExam.objects.all()

    serializer_class = (
        OnlineExamSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]