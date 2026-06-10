from django.urls import (
    include,
    path
)

urlpatterns = [

    path(
        "mandatory-public-disclosures/",
        include(
            "apps.compliance.mandatory_public_disclosures.urls"
        )
    ),

    path(
        "compliance-documents/",
        include(
            "apps.compliance.compliance_documents.urls"
        )
    ),

    path(
        "affiliations/",
        include(
            "apps.compliance.affiliations.urls"
        )
    ),

    path(
        "recognitions/",
        include(
            "apps.compliance.recognitions.urls"
        )
    ),


    path(
        "certificates/",
        include(
            "apps.compliance.certificates.urls"
        )
    ),


    path(
        "inspections/",
        include(
            "apps.compliance.inspections.urls"
        )
    ),

]