from rest_framework.views import APIView
from rest_framework.response import Response

from .services import monthly_collection_chart_service


class MonthlyCollectionChartView(APIView):

    def get(self, request):

        data = monthly_collection_chart_service()

        return Response(data)