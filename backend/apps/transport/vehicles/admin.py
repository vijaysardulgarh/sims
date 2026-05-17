from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        "vehicle_number",
        "vehicle_type",
        "capacity",
        "active",
    )

    search_fields = (
        "vehicle_number",
        "registration_number",
    )