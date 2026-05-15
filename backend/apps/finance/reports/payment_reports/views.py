from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    today_collection_service,
    payment_mode_service,
)


class TodayCollectionView(APIView):

    def get(self, request):

        data = today_collection_service()

        return Response(data)


class PaymentModeSummaryView(APIView):

    def get(self, request):

        data = payment_mode_service()

        return Response(data)