from rest_framework import viewsets

from .models import (
    ExamTimetable,
)

from .serializers import (
    ExamTimetableSerializer,
)


class ExamTimetableViewSet(
    viewsets.ModelViewSet
):

    queryset = ExamTimetable.objects.filter(
        is_deleted=False,
    )

    serializer_class = (
        ExamTimetableSerializer
    )

    search_fields = [
        "name",
        "code",
    ]

    ordering_fields = [
        "name",
        "start_date",
        "created_at",
    ]

    ordering = [
        "-start_date",
    ]

    def perform_create(
        self,
        serializer,
    ):

        serializer.save(
            created_by=self.request.user,
        )

    def perform_update(
        self,
        serializer,
    ):

        serializer.save(
            updated_by=self.request.user,
        )

    def perform_destroy(
        self,
        instance,
    ):

        instance.is_deleted = True

        instance.deleted_by = (
            self.request.user
        )

        instance.save()