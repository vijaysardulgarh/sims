# =============================================================================
# associations/views/smc_member_viewset.py
# =============================================================================

from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.associations.smc.models import (
    SMCMember
)

from apps.associations.smc.serializers import (
    SMCMemberSerializer
)


class SMCMemberViewSet(
    SchoolFilteredViewSet
):

    # ============================================
    # SERIALIZER
    # ============================================

    serializer_class = (
        SMCMemberSerializer
    )

    # ============================================
    # QUERYSET
    # ============================================

    queryset = (

        SMCMember.objects

        .filter(
            is_deleted=False
        )

        .order_by(
            "priority",
            "name"
        )

    )

    # ============================================
    # OVERRIDE QUERYSET
    # ============================================

    def get_queryset(self):

        return (

            SMCMember.objects

            .filter(
                is_deleted=False
            )

            .order_by(
                "priority",
                "name"
            )

        )

    # ============================================
    # SEARCH
    # ============================================

    search_fields = [

        "name",
        "position",
        "contact_number",
        "email",

    ]

    # ============================================
    # FILTERS
    # ============================================

    filterset_fields = [

        "position",
        "gender",
        "category",
        "show_on_website",

    ]

    # ============================================
    # ORDERING
    # ============================================

    ordering_fields = [

        "name",
        "priority",
        "nomination_date",
        "tenure_end_date",
        "created_at",

    ]

    ordering = [

        "priority",
        "name",

    ]