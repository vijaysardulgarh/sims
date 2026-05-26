from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.students.profiles.models import (
    Achiever
)

from apps.students.serializers import (
    AchieverSerializer
)

from apps.accounts.authorization.permissions import (
    CanViewStudents
)


# =========================================
# ACHIEVER LIST API VIEW
# =========================================

class AchieverListAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request):

        achievers = (

            Achiever.objects

            .select_related(
                "school",
                "achievement",
                "created_by",
                "updated_by",
            )

            .filter(
                is_deleted=False
            )

            .order_by("-created_at")
        )

        serializer = AchieverSerializer(

            achievers,

            many=True,
        )

        return Response(
            serializer.data
        )


# =========================================
# ACHIEVER DETAIL API VIEW
# =========================================

class AchieverDetailAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request, pk):

        achiever = get_object_or_404(

            Achiever.objects

            .select_related(
                "school",
                "achievement",
                "created_by",
                "updated_by",
            )

            .filter(
                is_deleted=False
            ),

            pk=pk,
        )

        serializer = AchieverSerializer(
            achiever
        )

        return Response(
            serializer.data
        )