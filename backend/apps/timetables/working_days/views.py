from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WorkingDay
from .serializers import WorkingDaySerializer


class WorkingDayListView(APIView):

    def get(self, request):

        queryset = WorkingDay.objects.filter(
            is_deleted=False,
        ).order_by(
            "display_order",
        )

        serializer = WorkingDaySerializer(
            queryset,
            many=True,
        )

        return Response(serializer.data)


class WorkingDayBulkUpdateView(APIView):

    @transaction.atomic
    def post(self, request):

        for item in request.data:

            obj = None

            # Update existing record if ID is present
            if item.get("id"):

                obj = WorkingDay.objects.filter(
                    pk=item["id"],
                    is_deleted=False,
                ).first()

            # If no ID, try to find by day_code
            if obj is None:

                obj = WorkingDay.objects.filter(
                    day_code=item["day_code"],
                    is_deleted=False,
                ).first()

            if obj:

                serializer = WorkingDaySerializer(
                    obj,
                    data=item,
                    partial=True,
                )

            else:

                serializer = WorkingDaySerializer(
                    data=item,
                )

            serializer.is_valid(
                raise_exception=True,
            )

            serializer.save(
                updated_by=request.user,
            )

        return Response(
            {
                "message": "Working days saved successfully."
            },
            status=status.HTTP_200_OK,
        )