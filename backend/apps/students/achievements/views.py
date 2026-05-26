from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.students.achievements.models import (
    Achievement
)

from apps.students.achievements.serializers import (
    AchievementSerializer
)

from apps.accounts.authorization.permissions import (
    CanViewStudents
)


# =========================================
# ACHIEVEMENT LIST API VIEW
# =========================================

class AchievementListAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request):

        achievements = (

            Achievement.objects

            .select_related(
                "school",
                "created_by",
                "updated_by",
            )

            .filter(
                is_deleted=False
            )

            .order_by("-date")
        )

        serializer = AchievementSerializer(

            achievements,

            many=True,
        )

        return Response(
            serializer.data
        )


# =========================================
# ACHIEVEMENT DETAIL API VIEW
# =========================================

class AchievementDetailAPIView(APIView):

    permission_classes = [
        CanViewStudents
    ]

    def get(self, request, pk):

        achievement = get_object_or_404(

            Achievement.objects

            .select_related(
                "school",
                "created_by",
                "updated_by",
            )

            .filter(
                is_deleted=False
            ),

            pk=pk,
        )

        serializer = AchievementSerializer(
            achievement
        )

        return Response(
            serializer.data
        )