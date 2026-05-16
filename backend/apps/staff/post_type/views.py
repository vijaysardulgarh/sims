from rest_framework.views import APIView
from rest_framework.response import Response

from apps.staff.post_type.models import PostType

from .serializers import (
    PostTypeSerializer
)


class PostTypeListAPIView(APIView):

    def get(self, request):

        queryset = (
            PostType.objects
            .all()
            .order_by("name")
        )

        serializer = PostTypeSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)