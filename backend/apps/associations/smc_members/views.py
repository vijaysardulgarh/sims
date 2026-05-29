from rest_framework.viewsets import (
    ModelViewSet
)

from apps.associations.smc_members.models import (
    SMCMember
)

from apps.associations.smc_members.serializers import (
    SMCMemberSerializer
)


class SMCMemberViewSet(
    ModelViewSet
):

    serializer_class = (
        SMCMemberSerializer
    )

    queryset = (

        SMCMember.objects.all()

        .order_by(
            "priority",
            "name"
        )

    )