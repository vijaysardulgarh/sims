from django.contrib import admin

from .models import (
    SeatingPlan
)


@admin.register(
    SeatingPlan
)
class SeatingPlanAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "exam",

        "room_number",

        "row_number",

        "seat_number",
    ]

    search_fields = [

        "student__full_name",

        "room_number",

        "seat_number",
    ]

    list_filter = [

        "exam",

        "room_number",
    ]