from rest_framework.views import APIView
from rest_framework.response import Response

from .services import finance_dashboard_service


class FinanceDashboardView(APIView):

    def get(self, request):

        data = finance_dashboard_service()

        return Response(data)