from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.core.utils import get_current_school
from apps.website.models import (
    AboutSchool,
    Principal,
    Affiliation,
    MandatoryPublicDisclosure,
    FAQ
)
from apps.schools.models import School


# =========================================
# ABOUT SCHOOL
# =========================================
class AboutSchoolAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        about = AboutSchool.objects.filter(school=school).first()

        if not about:
            return Response({"about": None})

        return Response({
            "description": about.description,
            "vision": getattr(about, "vision", ""),
            "mission": getattr(about, "mission", "")
        })


# =========================================
# PRINCIPAL MESSAGE
# =========================================
class PrincipalAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)

        message = (
            Principal.objects.filter(school=school).first()
            if school else Principal.objects.first()
        )

        if not message:
            return Response({"message": None})

        return Response({
            "name": message.name,
            "message": message.message,
            "photo": getattr(message, "photo", None)
        })


# =========================================
# AFFILIATION STATUS
# =========================================
class AffiliationAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        affiliations = Affiliation.objects.filter(school=school)

        return Response(list(affiliations.values()))


# =========================================
# INFRASTRUCTURE
# =========================================
class InfrastructureAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        infrastructures = school.infrastructures.all().order_by("category")

        data = [
            {
                "id": i.id,
                "name": i.name,
                "category": i.category,
                "description": getattr(i, "description", "")
            }
            for i in infrastructures
        ]

        return Response(data)


# =========================================
# MANDATORY DISCLOSURE
# =========================================
class MandatoryDisclosureAPIView(APIView):

    def get(self, request):

        disclosures = MandatoryPublicDisclosure.objects.filter(
            is_active=True
        ).order_by("id")

        return Response(list(disclosures.values()))


# =========================================
# FAQ
# =========================================
class FAQAPIView(APIView):

    def get(self, request):

        faqs = FAQ.objects.filter(is_active=True).order_by("order", "category")

        categories = {}

        for faq in faqs:
            cat = faq.get_category_display()

            if cat not in categories:
                categories[cat] = []

            categories[cat].append({
                "question": faq.question,
                "answer": faq.answer
            })

        return Response(categories)


# =========================================
# STATIC CONTENT FLAGS
# =========================================
class StaticPagesAPIView(APIView):

    def get(self, request):

        return Response({
            "achievements": True,
            "board_results": True,
            "sports_achievements": True
        })


# =========================================
# CONTACT
# =========================================
class ContactAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)

        if not school:
            return Response({"contact": None})

        return Response({
            "name": school.name,
            "address": getattr(school, "address", ""),
            "phone": getattr(school, "phone_number", ""),
            "email": getattr(school, "email", "")
        })