from rest_framework.viewsets import (
    ModelViewSet
)

from .models import SchoolSetting

from .serializers import (
    SchoolSettingSerializer
)


class SchoolSettingViewSet(
    ModelViewSet
):

    queryset = (
        SchoolSetting.objects
        .select_related("school")
    )

    serializer_class = (
        SchoolSettingSerializer
    )