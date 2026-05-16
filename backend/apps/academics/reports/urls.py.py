from django.urls import (
    include,
    path
)

urlpatterns = [

    # =====================================
    # SUBJECT STRENGTH REPORT
    # =====================================

    path(
        "subject-strength/",
        include(
            "apps.academics.reports.subject_strength.urls"
        )
    ),

    # =====================================
    # SUBJECTS OFFERED REPORT
    # =====================================

    path(
        "subjects-offered/",
        include(
            "apps.academics.reports.subjects_offered.urls"
        )
    ),

    # =====================================
    # TEACHER WORKLOAD REPORT
    # =====================================

    path(
        "teacher-workload/",
        include(
            "apps.academics.reports.teacher_workload.urls"
        )
    ),

    # =====================================
    # TIMETABLE ENTRY REPORT
    # =====================================

    path(
        "timetable-entry/",
        include(
            "apps.academics.reports.timetable_entry.urls"
        )
    ),
]