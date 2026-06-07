from django.contrib import admin

from apps.infrastructure.classrooms.models import (
    Classroom
)


@admin.register(Classroom)
class ClassroomAdmin(
    admin.ModelAdmin
):

    list_display = (

        "classroom_code",

        "room",

        "floor",

        "capacity",

        "smart_classroom",

        "internet_enabled",

        "is_active",
    )

    list_display_links = (

        "classroom_code",
    )

    search_fields = (

        "classroom_code",

        "room__room_name",

        "room__room_number",
    )

    list_filter = (

        "smart_classroom",

        "air_conditioned",

        "projector_available",

        "internet_enabled",

        "is_active",
    )

    autocomplete_fields = (

        "room",

        "floor",
    )

    ordering = (

        "classroom_code",
    )

    list_per_page = 25

    readonly_fields = (

        "created_at",

        "updated_at",

        "created_by",

        "updated_by",
    )