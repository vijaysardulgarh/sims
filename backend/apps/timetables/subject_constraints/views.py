from django.db import transaction

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    SubjectConstraint,
)

from .serializers import (
    SubjectConstraintSerializer,
)


class SubjectConstraintListView(
    ListAPIView,
):

    serializer_class = (
        SubjectConstraintSerializer
    )

    queryset = (
        SubjectConstraint.objects.filter(
            is_deleted=False,
        ).select_related(
            "subject_requirement",
            "subject_requirement__school_class",
            "subject_requirement__section",
            "subject_requirement__subject",
        ).order_by(
            "subject_requirement__school_class__display_order",
            "subject_requirement__subject__name",
        )
    )

    search_fields = [
        "subject_requirement__school_class__name",
        "subject_requirement__section__name",
        "subject_requirement__subject__name",
    ]

    ordering_fields = [
        "priority",
        "subject_requirement__school_class__display_order",
        "subject_requirement__subject__name",
    ]


class SubjectConstraintBulkSaveView(
    APIView,
):

    @transaction.atomic
    def post(
        self,
        request,
    ):

        rows = request.data

        if not isinstance(
            rows,
            list,
        ):

            return Response(
                {
                    "detail": (
                        "Expected a list of records."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        saved = []

        for row in rows:

            instance = None

            if row.get("id"):

                instance = SubjectConstraint.objects.filter(
                    id=row["id"],
                    is_deleted=False,
                ).first()

            serializer = (
                SubjectConstraintSerializer(
                    instance=instance,
                    data=row,
                )
            )

            serializer.is_valid(
                raise_exception=True,
            )

            serializer.save(

                created_by=(
                    request.user
                    if instance is None
                    else serializer.instance.created_by
                ),

                updated_by=request.user,

            )

            saved.append(
                serializer.data
            )

        return Response(
            saved,
            status=status.HTTP_200_OK,
        )