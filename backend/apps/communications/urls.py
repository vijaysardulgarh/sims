from django.urls import (
    include,
    path,
)

urlpatterns = [

    path(
        '',
        include(
            'apps.communications.communication_categories.urls'
        )
    ),

    path(
        '',
        include(
            'apps.communications.communication_templates.urls'
        )
    ),

    path(
        '',
        include(
            'apps.communications.notifications.urls'
        )
    ),

    path(
        '',
        include(
            'apps.communications.circulars.urls'
        )
    ),

    path(
        '',
        include(
            'apps.communications.notices.urls'
        )
    ),

    path(
        '',
        include(
            'apps.communications.news.urls'
        )
    ),

    path(
        '',
        include(
            'apps.communications.events.urls'
        )
    ),

]