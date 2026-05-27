# =============================================================================
# associations/views/smc_member_views.py
# =============================================================================

from rest_framework.permissions import IsAuthenticated

from apps.associations.smc_members.models import SMCMember
from apps.core.common.views import BaseAPIView


class SMCMemberAPIView(BaseAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(request, "school", None)

        if not school:

            return self.error_response(
                message="School not found.",
                status_code=400
            )

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        queryset = (

            SMCMember.objects.filter(
                school=school,
                academic_session=academic_session,
                is_active=True,
                is_deleted=False
            )

            .order_by(
                "priority",
                "name"
            )
        )

        data = list(

            queryset.values(
                "id",
                "name",
                "position",
                "contact_number",
                "email",
                "show_on_website",
            )
        )

        return self.success_response(data=data)