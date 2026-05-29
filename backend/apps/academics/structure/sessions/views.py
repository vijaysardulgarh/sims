# =============================================================================
# academics/sessions/views/academic_session_views.py
# =============================================================================

from apps.core.common.views import (
    SchoolFilteredViewSet
)

from apps.academics.structure.sessions.models import (
    AcademicSession
)

from apps.academics.structure.sessions.serializers import (
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