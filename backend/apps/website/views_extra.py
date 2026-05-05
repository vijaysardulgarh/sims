from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from django.http import FileResponse, Http404
import os


# =========================================
# ADMISSION FORM (PDF DOWNLOAD)
# =========================================
class AdmissionFormAPIView(APIView):

    def get(self, request):

        file_path = os.path.join(settings.BASE_DIR, "static", "admission_form.pdf")

        if not os.path.exists(file_path):
            raise Http404("Admission form not found.")

        return FileResponse(open(file_path, "rb"), content_type="application/pdf")


# =========================================
# STATIC WEBSITE PAGES
# =========================================
class WebsitePagesAPIView(APIView):

    def get(self, request):

        return Response({
            "gallery": True,
            "notices": True,
            "events": True,
            "syllabus": True,
            "management": True,
            "curriculum": True,
            "exams_results": True,
            "academic_calendar": True,
            "downloads": True,
            "admission_procedure": True,
            "statistics": True,
        })


# =========================================
# DASHBOARD (AUTH REQUIRED)
# =========================================
class DashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "message": "Welcome to Dashboard",
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            }
        })