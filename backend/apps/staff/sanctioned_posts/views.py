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
    ]

    # ============================================
    # SEARCH
    # ============================================

    search_fields = [

        "school__name",

        "post_type__name",
    ]

    # ============================================
    # ORDERING
    # ============================================

    ordering_fields = [

        "post_type__name",

        "sanctioned_posts",

        "regular_working",

        "guest_working",

        "hkrnl_working",
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