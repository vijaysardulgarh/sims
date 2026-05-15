from django.urls import (
    include,
    path
)

urlpatterns = [

    # =====================================
    # CORE ACADEMICS
    # =====================================

    path(
        "classes/",
        include(
            "apps.academics.classes.urls"
        )
    ),

    path(
        "streams/",
        include(
            "apps.academics.streams.urls"
        )
    ),

    path(
        "mediums/",
        include(
            "apps.academics.mediums.urls"
        )
    ),

    path(
        "classrooms/",
        include(
            "apps.academics.classrooms.urls"
        )
    ),

    path(
        "sections/",
        include(
            "apps.academics.sections.urls"
        )
    ),

    path(
        "subjects/",
        include(
            "apps.academics.subjects.urls"
        )
    ),

    path(
        "class-subjects/",
        include(
            "apps.academics.class_subjects.urls"
        )
    ),

    path(
        "days/",
        include(
            "apps.academics.days.urls"
        )
    ),

    # =====================================
    # TIMETABLE MANAGEMENT
    # =====================================

    path(
        "teacher-subject-assignments/",
        include(
            "apps.academics.teacher_subject_assignments.urls"
        )
    ),

    path(
        "timetable-slots/",
        include(
            "apps.academics.timetable_slots.urls"
        )
    ),

    path(
        "timetables/",
        include(
            "apps.academics.timetables.urls"
        )
    ),

    path(
        "timetable-generator/",
        include(
            "apps.academics.timetable_generator.urls"
        )
    ),

    # =====================================
    # REPORTS
    # =====================================

    path(
        "reports/",
        include(
            "apps.academics.reports.urls"
        )
    ),
]