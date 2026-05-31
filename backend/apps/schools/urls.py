from django.urls import (
    path,
    include
)

urlpatterns = [

    path(
        "schools/",
        include(
            "apps.schools.schools.urls"
        )
    ),

    path(
        "about-schools/",
        include(
            "apps.schools.about-school.urls"
        )
    ),

    path(
        "principals/",
        include(
            "apps.schools.principals.urls"
        )
    ),

    path(
        "galleries/",
        include(
            "apps.schools.galleries.urls"
        )
    ),

    path(
        "branches/",
        include(
            "apps.schools.branches.urls"
        )
    ),

    path(
        "school-settings/",
        include(
            "apps.schools.school-settings.urls"
        )
    ),

]