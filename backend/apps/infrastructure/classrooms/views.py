from rest_framework import viewsets

from apps.infrastructure.classrooms.models import (
    Classroom
)

from apps.infrastructure.classrooms.serializers import (
    ClassroomSerializer
)


class ClassroomViewSet(
    viewsets.ModelViewSet
):

    serializer_class = (
        ClassroomSerializer
    )

    queryset = (

        Classroom.objects

        .select_related(
            "room",
            "floor",
            "school"
        )

        .filter(
            is_deleted=False
        )
    )

    def get_queryset(
        self
    ):

        queryset = (
            super()
            .get_queryset()
        )

        room = (
            self.request
            .query_params
            .get("room")
        )

        floor = (
            self.request
            .query_params
            .get("floor")
        )

        if room:

            queryset = queryset.filter(
                room_id=room
            )

        if floor:

            queryset = queryset.filter(
                floor_id=floor
            )

        return queryset

    def perform_create(
        self,
        serializer
    ):

        serializer.save(

            school=(
                self.request.school
            ),

            created_by=(
                self.request.user
            ),

            updated_by=(
                self.request.user
            )
        )

    def perform_update(
        self,
        serializer
    ):

        serializer.save(

            updated_by=(
                self.request.user
            )
        )