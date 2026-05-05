from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.schools.models import School


class DocumentDetailAPIView(APIView):

    def get(self, request, school_id):

        school = get_object_or_404(School, pk=school_id)

        documents = school.documents.all()

        return Response({
            "school": school.name,
            "documents": list(documents.values())
        })