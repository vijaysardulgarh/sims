from rest_framework.views import APIView
from rest_framework.response import Response
from apps.finance.models import FeeStructure


class FeeStructureAPIView(APIView):

    def get(self, request):

        data = []

        for f in FeeStructure.objects.select_related("student_class", "stream"):
            data.append({
                "class": f.student_class.name,
                "stream": f.stream.name if f.stream else None,
                "amount": f.amount
            })

        return Response(data)