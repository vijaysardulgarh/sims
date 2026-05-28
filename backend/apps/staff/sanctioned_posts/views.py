from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated
)

from apps.staff.sanctioned_posts.models import (
    SanctionedPost
)

from .serializers import (
    SanctionedPostSerializer
)


class SanctionedPostViewSet(
    viewsets.ModelViewSet
):

    # ============================================
    # SERIALIZER
    # ============================================

    serializer_class = (
        SanctionedPostSerializer
    )

    # ============================================
    # PERMISSIONS
    # ============================================

    permission_classes = [
        IsAuthenticated
    ]

    # ============================================
    # QUERYSET
    # ============================================

    queryset = (

        SanctionedPost.objects

        .select_related(

            "school",

            "post_type",

            "subject",
        )

        .filter(
            is_deleted=False
        )

        .order_by(
            "post_type__name"
        )
    )

    # ============================================
    # FILTERS
    # ============================================

    filterset_fields = [

        "school",

        "post_type",

        "subject",
    ]

    # ============================================
    # SEARCH
    # ============================================

    search_fields = [

        "designation",

        "school__name",

        "post_type__name",

        "subject__name",
    ]

    # ============================================
    # ORDERING
    # ============================================

    ordering_fields = [

        "total_posts",
    ]

    ordering = [
        "post_type__name"
    ]

    # ============================================
    # SOFT DELETE
    # ============================================

    def perform_destroy(
        self,
        instance
    ):

        instance.is_deleted = True

        instance.save()