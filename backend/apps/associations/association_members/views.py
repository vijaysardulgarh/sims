# =============================================================================
# association_members/views.py
# =============================================================================

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.association_members.models import (
    AssociationMember
)

from apps.associations.association_members.serializers import (
    AssociationMemberSerializer
)

from apps.core.common.views import (
    BaseAPIView
)


class AssociationMemberAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        queryset = (

            AssociationMember.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False,
            )

            .select_related(

                "association",

                "staff",
            )

            .order_by(

                "designation",

                "staff__name"
            )
        )

        serializer = (

            AssociationMemberSerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )