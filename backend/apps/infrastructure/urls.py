from django.urls import (
    include,
    path
)

urlpatterns = [


    path(
        "buildings/",
        include(
            "apps.infrastructure.buildings.urls"
        )
    ),

    path(
        "floors/",
        include(
            "apps.infrastructure.floors.urls"
        )
    ),

    path(
        "rooms/",
        include(
            "apps.infrastructure.rooms.urls"
        )
    ),


    path(
        "classrooms/",
        include(
            "apps.infrastructure.classrooms.urls"
        )
    ),    
]