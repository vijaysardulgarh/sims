from django.contrib import admin

from .models import (
    CompetencyAssessment
)


@admin.register(
    CompetencyAssessment
)
class CompetencyAssessmentAdmin(
    admin.ModelAdmin
):

    list_display = [

        "student",

        "subject",

        "exam",

        "knowledge_grade",

        "application_grade",
    ]

    search_fields = [

        "student__full_name",

        "subject__name",
    ]

    list_filter = [

        "exam",

        "subject",
    ]