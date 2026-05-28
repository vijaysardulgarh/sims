from rest_framework import viewsets

from apps.staff.post_type.models import PostType

from .serializers import PostTypeSerializer


class PostTypeViewSet(viewsets.ModelViewSet):

    queryset = (
        PostType.objects
        .all()
        .order_by("name")
    )

    serializer_class = PostTypeSerializer