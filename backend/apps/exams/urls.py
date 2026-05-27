# =============================================================================
# project/urls.py
# =============================================================================

from django.contrib import admin

from django.urls import (
    path,
    include
)

urlpatterns = [

    # =====================================
    # DJANGO ADMIN
    # =====================================

    path(
        "admin/",
        admin.site.urls
    ),


    # =====================================
    # EXAMS
    # =====================================

    path(
        "api/exams/",
        include("apps.exams.urls")
    ),

    path(
        "api/exam-types/",
        include("apps.exams.exam_types.urls")
    ),

    path(
        "api/exam-notifications/",
        include("apps.exams.exam_notifications.urls")
    ),

    path(
        "api/online-exams/",
        include("apps.exams.online_exams.urls")
    ),

    path(
        "api/exam-schedules/",
        include("apps.exams.exam_schedules.urls")
    ),
]