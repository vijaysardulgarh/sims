from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.exams.models import ExamNotification
from apps.exams.serializers import (
    ExamNotificationSerializer
)


# =====================================
# EXAM NOTIFICATION LIST / CREATE
# =====================================

class ExamNotificationListCreateAPIView(
    generics.ListCreateAPIView
):

    queryset = ExamNotification.objects.all().order_by(
        "-created_at"
    )

    serializer_class = (
        ExamNotificationSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]


# =====================================
# EXAM NOTIFICATION DETAIL
# =====================================

class ExamNotificationDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = ExamNotification.objects.all()

    serializer_class = (
        ExamNotificationSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]