from django.urls import (
    include,
    path,
)

urlpatterns = [

    path(
        "generate/",
        include(
            "apps.timetables.timetable_designer.generate.urls"
        )
    ),

    path(
        "movement/",
        include(
            "apps.timetables.timetable_designer.movement.urls"
        )
    ),

    path(
        "assignments/",
        include(
            "apps.timetables.timetable_designer.assignments.urls"
        )
    ),

    path(
        "grid/",
        include(
            "apps.timetables.timetable_designer.grid.urls"
        )
    ),

    path(
        "conflicts/",
        include(
            "apps.timetables.timetable_designer.conflicts.urls"
        )
    ),

    path(
        "publishing/",
        include(
            "apps.timetables.timetable_designer.publishing.urls"
        )
    ),

]