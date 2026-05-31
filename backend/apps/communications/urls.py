from django.urls import (
    include,
    path
)

urlpatterns = [

    path(
        "news/",
        include(
            "apps.communications.news.urls"
        )
    ),

    path(
        "events/",
        include(
            "apps.communications.events.urls"
        )
    ),

    path(
        "notices/",
        include(
            "apps.communications.notices.urls"
        )
    ),

    path(
        "circulars/",
        include(
            "apps.communications.circulars.urls"
        )
    ),
]