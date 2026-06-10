from rest_framework import viewsets

from .models import (
    TeacherAvailability,
)

from .serializers import (
    TeacherAvailabilitySerializer,
)


class TeacherAvailabilityViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        TeacherAvailability.objects.filter(
            is_deleted=False,
        )
    )

    serializer_class = (
        TeacherAvailabilitySerializer
    )

    search_fields = [
        "teacher__first_name",
        "teacher__last_name",
    ]

    ordering_fields = [
        "day",
        "created_at",
    ]

    ordering = [
        "teacher",
        "day",
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