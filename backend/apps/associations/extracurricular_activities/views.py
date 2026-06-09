# =============================================================================
# associations/views/extracurricular_activity_views.py
# =============================================================================

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.associations.extracurricular_activities.models import (
    ExtracurricularActivity
)

from apps.associations.extracurricular_activities.serializers import (
    ExtracurricularActivitySerializer
)

from apps.core.common.views import (
    BaseAPIView
)


class ExtracurricularActivityAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    # =========================================================
    # LIST / DETAIL
    # =========================================================

    def get(
        self,
        request,
        pk=None
    ):

        school = getattr(
            request,
            "school",
            None
        )

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        queryset = (

            ExtracurricularActivity.objects

            .filter(
                school=school,
                academic_session=academic_session,
                is_deleted=False,
            )

            .select_related(
                "coordinator",
                "academic_session",
            )

            .prefetch_related(
                "participants"
            )
        )

        if pk:

            activity = queryset.filter(
                pk=pk
            ).first()

            if not activity:

                return self.error_response(
                    message="Activity not found",
                    status_code=404
                )

            serializer = (
                ExtracurricularActivitySerializer(
                    activity
                )
            )

            return self.success_response(
                data=serializer.data
            )

        queryset = queryset.order_by(
            "priority",
            "name"
        )

        serializer = (
            ExtracurricularActivitySerializer(
                queryset,
                many=True
            )
        )

        return self.success_response(
            data=serializer.data
        )

    # =========================================================
    # CREATE
    # =========================================================

    def post(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        academic_session = getattr(
            request,
            "academic_session",
            None
        )

        serializer = (
            ExtracurricularActivitySerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            activity = serializer.save(

                school=school,

                academic_session=
                academic_session
            )

            return self.success_response(

                data=
                ExtracurricularActivitySerializer(
                    activity
                ).data,

                message=
                "Activity created successfully"
            )

        return self.error_response(

            errors=
            serializer.errors,

            status_code=400
        )

    # =========================================================
    # UPDATE
    # =========================================================

    def put(
        self,
        request,
        pk
    ):

        activity = (

            ExtracurricularActivity.objects

            .filter(
                pk=pk,
                is_deleted=False
            )

            .first()
        )

        if not activity:

            return self.error_response(
                message="Activity not found",
                status_code=404
            )

        serializer = (
            ExtracurricularActivitySerializer(
                activity,
                data=request.data,
                partial=True
            )
        )

        if serializer.is_valid():

            serializer.save()

            return self.success_response(

                data=serializer.data,

                message=
                "Activity updated successfully"
            )

        return self.error_response(

            errors=
            serializer.errors,

            status_code=400
        )

    # =========================================================
    # DELETE
    # =========================================================

    def delete(
        self,
        request,
        pk
    ):

        activity = (

            ExtracurricularActivity.objects

            .filter(
                pk=pk,
                is_deleted=False
            )

            .first()
        )

        if not activity:

            return self.error_response(
                message="Activity not found",
                status_code=404
            )

        activity.is_deleted = True
        activity.is_active = False

        activity.save()

        return self.success_response(
            message=
            "Activity deleted successfully"
        )