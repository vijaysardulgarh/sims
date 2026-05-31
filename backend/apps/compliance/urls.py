from django.urls import (
    include,
    path
)

urlpatterns = [

    path(
        "mandatory-public-disclosures/",
        include(
            "apps.compliance.mandatory-public-disclosures.urls"
        )
    ),

    path(
        "compliance-documents/",
        include(
            "apps.compliance.compliance-documents.urls"
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