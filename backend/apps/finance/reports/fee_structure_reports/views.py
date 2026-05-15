from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    pending_fee_report_service,
    fully_paid_report_service,
)


class PendingFeeReportView(APIView):

    def get(self, request):

        data = pending_fee_report_service()

        return Response(data)


class FullyPaidReportView(APIView):

    def get(self, request):

        data = fully_paid_report_service()

        return Response(data)