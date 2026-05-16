from django.contrib import admin

from apps.staff.models import ClassIncharge


@admin.register(ClassIncharge)
class ClassInchargeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "section",
        "staff",
        "effective_from",
        "effective_to",
        "active",
    )

    search_fields = (
        "staff__name",
        "section__name",
    )

    list_filter = (
        "active",
        "effective_from",
    )

    ordering = (
        "-effective_from",
    )

    list_per_page = 25