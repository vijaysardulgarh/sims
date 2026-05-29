from django.urls import (
    include,
    path
)

urlpatterns = [

    # =====================================
    # STRUCTURE
    # =====================================

    path(
        "classes/",
        include(
            "apps.academics.structure.classes.urls"
        )
    ),

    path(
        "streams/",
        include(
            "apps.academics.structure.streams.urls"
        )
    ),

    path(
        "mediums/",
        include(
            "apps.academics.structure.mediums.urls"
        )
    ),

    path(
        "classrooms/",
        include(
            "apps.academics.structure.classrooms.urls"
        )
    ),

    path(
        "sections/",
        include(
            "apps.academics.structure.sections.urls"
        )
    ),

    path(
        "sessions/",
        include(
            "apps.academics.structure.sessions.urls"
        )
    ),

    # =====================================
    # CURRICULUM
    # =====================================

    path(
        "subjects/",
        include(
            "apps.academics.curriculum.subjects.urls"
        )
    ),

    path(
        "class-subjects/",
        include(
            "apps.academics.curriculum.class_subjects.urls"
        )
    ),

    path(
        "teacher-subject-assignments/",
        include(
            "apps.academics.curriculum.teacher_subject_assignments.urls"
        )
    ),

    # =====================================
    # TIMETABLE
    # =====================================

    path(
        "days/",
        include(
            "apps.academics.timetable.days.urls"
        )
    ),

    path(
        "timetable-slots/",
        include(
            "apps.academics.timetable.timetable_slots.urls"
        )
    ),

    path(
        "timetables/",
        include(
            "apps.academics.timetable.timetables.urls"
        )
    ),

    path(
        "timetable-generator/",
        include(
            "apps.academics.timetable.timetable_generator.urls"
        )
    ),

    path(
        "timetable-drag-drop/",
        include(
            "apps.academics.timetable.timetable_drag_drop.urls"
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