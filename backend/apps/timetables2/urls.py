from django.urls import (
    include,
    path
)

urlpatterns = [

    path(
        "class-subjects/",
        include(
            "apps.timetables.class_subjects.urls"
        )
    ),

    path(
        "teacher-subject-assignments/",
        include(
            "apps.timetables.teacher_subject_assignments.urls"
        )
    ),

    # =====================================
    # TIMETABLE
    # =====================================

    path(
        "days/",
        include(
            "apps.timetable.days.urls"
        )
    ),

    path(
        "timetable-slots/",
        include(
            "apps.timetable.timetable_slots.urls"
        )
    ),

    path(
        "timetables/",
        include(
            "apps.timetable.timetables.urls"
        )
    ),

    path(
        "timetable-generator/",
        include(
            "apps.timetable.timetable_generator.urls"
        )
    ),

    path(
        "timetable-drag-drop/",
        include(
            "apps.timetable.timetable_drag_drop.urls"
        )
    ),

    path(
        "classrooms/",
        include(
            "apps.timetable.classrooms.urls"
        )
    ),    
]