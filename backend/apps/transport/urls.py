from django.urls import path, include

urlpatterns = [
    path(
        "vehicles/",
        include("apps.transport.vehicles.urls")
    ),

    path(
        "drivers/",
        include("apps.transport.drivers.urls")
    ),

    path(
        "transport-routes/",
        include(
            "apps.transport.transport_routes.urls"
        )
    ),

    path(
        "transport-assignments/",
        include(
            "apps.transport.transport_assignments.urls"
        )
    ),
]