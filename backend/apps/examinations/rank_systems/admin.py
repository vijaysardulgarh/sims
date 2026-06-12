from django.contrib import admin

from .models import (
    RankSystem
)


@admin.register(
    RankSystem
)
class RankSystemAdmin(
    admin.ModelAdmin
):

    list_display = [

        "name",

        "exam",

        "rank_type",

        "rank_method",

        "is_active",
    ]

    search_fields = [

        "name",

        "exam__name",
    ]

    list_filter = [

        "rank_type",

        "rank_method",

        "is_active",
    ]