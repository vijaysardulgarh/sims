# =============================================================================
# associations/views/extracurricular_activity_views.py
# =============================================================================

from rest_framework.permissions import IsAuthenticated

from apps.associations.extracurricular_activities.models import (
    ExtracurricularActivity
)

from apps.core.common.views import BaseAPIView


class ExtracurricularActivityAPIView(
    BaseAPIView
):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        school = getattr(request, "school", None)

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        queryset = (

            ExtracurricularActivity.objects.filter(
                school=school,
                academic_session=academic_session,
                is_active=True,
                is_deleted=False,
            )

            .select_related(
                "coordinator",
                "academic_session",
            )

            .prefetch_related(
                "participants"
            )

            .order_by(
                "priority",
                "name"
            )
        )

        data = []

        for activity in queryset:

            data.append({

                "id":
                    activity.id,

                "name":
                    activity.name,

                "category":
                    activity.category,

                "status":
                    activity.status,

                "start_date":
                    activity.start_date,

                "end_date":
                    activity.end_date,

                "location":
                    activity.location,

                "coordinator":

                    activity.coordinator.name
                    if activity.coordinator
                    else None,

                "participants_count":

                    activity.participants.count(),
            })

        return self.success_response(data=data)