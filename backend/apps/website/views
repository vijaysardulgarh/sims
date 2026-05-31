from django.shortcuts import (
    get_object_or_404
)

from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from rest_framework.permissions import (
    IsAuthenticated
)

from apps.website.models import (

    AboutSchool,

    Principal,

    Affiliation,

    MandatoryPublicDisclosure,

    FAQ
)

from apps.schools.models import (
    School
)

from apps.core.common.views import (
    BaseAPIView
)


# =========================================
# ABOUT SCHOOL
# =========================================

class AboutSchoolAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        about = (

            AboutSchool.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .first()
        )

        if not about:

            return self.success_response(

                data={
                    "about": None
                }
            )

        return self.success_response(

            data={

                "description":
                    about.description,

                "vision":
                    getattr(
                        about,
                        "vision",
                        ""
                    ),

                "mission":
                    getattr(
                        about,
                        "mission",
                        ""
                    )
            }
        )


# =========================================
# PRINCIPAL MESSAGE
# =========================================

class PrincipalAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        message = (

            Principal.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .first()
        )

        if not message:

            return self.success_response(

                data={
                    "message": None
                }
            )

        return self.success_response(

            data={

                "name":
                    message.name,

                "message":
                    message.message,

                "photo":

                    getattr(
                        message,
                        "photo",
                        None
                    )
            }
        )


# =========================================
# AFFILIATION STATUS
# =========================================

class AffiliationAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        affiliations = (

            Affiliation.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("id")
        )

        return self.success_response(

            data=list(
                affiliations.values()
            )
        )


# =========================================
# INFRASTRUCTURE
# =========================================

class InfrastructureAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.error_response(

                message="School not found.",

                status_code=400
            )

        infrastructures = (

            school.infrastructures.filter(

                is_active=True,

                is_deleted=False
            )

            .order_by("category")
        )

        data = [

            {

                "id":
                    infrastructure.id,

                "name":
                    infrastructure.name,

                "category":
                    infrastructure.category,

                "description":

                    getattr(

                        infrastructure,

                        "description",

                        ""
                    )
            }

            for infrastructure
            in infrastructures
        ]

        return self.success_response(
            data=data
        )


# =========================================
# MANDATORY DISCLOSURE
# =========================================

class MandatoryDisclosureAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        disclosures = (

            MandatoryPublicDisclosure.objects

            .filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by("id")
        )

        return self.success_response(

            data=list(
                disclosures.values()
            )
        )


# =========================================
# FAQ
# =========================================

class FAQAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        faqs = (

            FAQ.objects.filter(

                school=school,

                is_active=True,

                is_deleted=False
            )

            .order_by(

                "order",

                "category"
            )
        )

        categories = {}

        for faq in faqs:

            category = (
                faq.get_category_display()
            )

            if category not in categories:

                categories[
                    category
                ] = []

            categories[
                category
            ].append({

                "question":
                    faq.question,

                "answer":
                    faq.answer
            })

        return self.success_response(
            data=categories
        )


# =========================================
# STATIC CONTENT FLAGS
# =========================================

class StaticPagesAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        return self.success_response(

            data={

                "achievements":
                    True,

                "board_results":
                    True,

                "sports_achievements":
                    True
            }
        )


# =========================================
# CONTACT
# =========================================

class ContactAPIView(
    BaseAPIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        school = getattr(
            request,
            "school",
            None
        )

        if not school:

            return self.success_response(

                data={
                    "contact": None
                }
            )

        return self.success_response(

            data={

                "name":
                    school.name,

                "address":

                    getattr(
                        school,
                        "address",
                        ""
                    ),

                "phone":

                    getattr(
                        school,
                        "phone",
                        ""
                    ),

                "email":

                    getattr(
                        school,
                        "email",
                        ""
                    )
            }
        )