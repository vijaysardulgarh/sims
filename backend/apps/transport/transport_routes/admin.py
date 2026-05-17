from django.contrib import admin

from .models import (
    TransportRoute,
    TransportStop,
)


class TransportStopInline(admin.TabularInline):

    model = TransportStop

    extra = 1


@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):

    list_display = (
        "route_name",
        "start_location",
        "end_location",
        "active",
    )

    inlines = [TransportStopInline]