# =============================================================================
# academics/sessions/views/academic_session_views.py
# =============================================================================

from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.sessions.models import (
    AcademicSession
)

from apps.academics.sessions.serializers import (
    AcademicSessionSerializer
)


class AcademicSessionViewSet(
    SchoolFilteredViewSet
):

    # ===========================================
    # SERIALIZER
    # ===========================================

    serializer_class = (
        AcademicSessionSerializer
    )

    # ===========================================
    # QUERYSET
    # ===========================================

    queryset = (
        AcademicSession.objects.all()
    )