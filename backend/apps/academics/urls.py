from django.urls import (
    include,
    path
)

urlpatterns = [

    # =====================================
    # STRUCTURE
    # =====================================

    path(
        "classes/",
        include(
            "apps.academics.classes.urls"
        )
    ),

    path(
        "streams/",
        include(
            "apps.academics.streams.urls"
        )
    ),

    path(
        "mediums/",
        include(
            "apps.academics.mediums.urls"
        )
    ),

    path(
        "sections/",
        include(
            "apps.academics.sections.urls"
        )
    ),

    path(
        "sessions/",
        include(
            "apps.academics.sessions.urls"
        )
    ),

    # =====================================
    # CURRICULUM
    # =====================================

    path(
        "subjects/",
        include(
            "apps.academics.subjects.urls"
        )
    ),
]