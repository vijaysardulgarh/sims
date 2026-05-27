from django.contrib import admin

from apps.exams.models import OnlineExam


@admin.register(OnlineExam)
class OnlineExamAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "exam",
        "duration_minutes",
        "total_questions",
        "negative_marking",
        "random_questions",
        "start_datetime",
        "end_datetime",
        "school",
    )

    list_filter = (
        "negative_marking",
        "random_questions",
        "school",
    )

    search_fields = (
        "exam__name",
        "instructions",
    )

    ordering = (
        "-id",
    )