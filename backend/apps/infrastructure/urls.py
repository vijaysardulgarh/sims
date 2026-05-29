from django.urls import (
    include,
    path
)

urlpatterns = [

    path(
        "classrooms/",
        include(
            "apps.infrastructure.classrooms.urls"
        )
    ),    
]