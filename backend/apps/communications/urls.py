from django.urls import (
    include,
    path,
)

urlpatterns = [

    path(
        "communication-categories/",
        include(
            "apps.communications.communication_categories.urls"
        )
    ),

    path(
        "communication-templates/",
        include(
            "apps.communications.communication_templates.urls"
        )
    ),

    path(
        "notifications/",
        include(
            "apps.communications.notifications.urls"
        )
    ),

    path(
        "circulars/",
        include(
            "apps.communications.circulars.urls"
        )
    ),

    path(
        "notices/",
        include(
            "apps.communications.notices.urls"
        )
    ),

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
        "faqs/",
        include(
            "apps.communications.faqs.urls"
        )
    ),

]