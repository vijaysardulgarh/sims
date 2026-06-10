from django.contrib import admin

from .models import (
    ResultApproval
)


@admin.register(
    ResultApproval
)
class ResultApprovalAdmin(
    admin.ModelAdmin
):

    list_display = [

        "result",

        "status",

        "approved_by",

        "approved_at",
    ]

    search_fields = [

        "result__student__full_name",

        "result__exam__name",
    ]

    list_filter = [

        "status",
    ]