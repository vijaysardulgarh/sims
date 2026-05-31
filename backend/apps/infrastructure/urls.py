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

    path(
        "laboratories/",
        include(
            "apps.infrastructure.laboratories.urls"
        )
    ),

    path(
        "libraries/",
        include(
            "apps.infrastructure.libraries.urls"
        )
    ),

    path(
        "auditoriums/",
        include(
            "apps.infrastructure.auditoriums.urls"
        )
    ),

    path(
        "playgrounds/",
        include(
            "apps.infrastructure.playgrounds.urls"
        )
    ),

    path(
        "asset-categories/",
        include(
            "apps.infrastructure.asset_categories.urls"
        )
    ),

    path(
        "assets/",
        include(
            "apps.infrastructure.assets.urls"
        )
    ),

    path(
        "maintenance-records/",
        include(
            "apps.infrastructure.maintenance_records.urls"
        )
    ),

    path(
        "facilities/",
        include(
            "apps.infrastructure.facilities.urls"
        )
    ),

]