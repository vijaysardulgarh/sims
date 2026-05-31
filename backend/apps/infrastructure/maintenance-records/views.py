from rest_framework.viewsets import (
    ModelViewSet
)

from .models import (
    MaintenanceRecord
)

from .serializers import (
    MaintenanceRecordSerializer
)


class MaintenanceRecordViewSet(
    ModelViewSet
):

    queryset = (

        MaintenanceRecord.objects
        .select_related(
            "school",
            "asset"
        )
    )

    serializer_class = (
        MaintenanceRecordSerializer
    )