from django.urls import (
    include,
    path,
)

urlpatterns = [

    path(
        "bell-schedules/",
        include(
            "apps.timetable.bell_schedules.urls"
        )
    ),

    path(
        "exam-timetables/",
        include(
            "apps.timetable.exam_timetables.urls"
        )
    ),

    path(
        "exam-timetable-entries/",
        include(
            "apps.timetable.exam_timetable_entries.urls"
        )
    ),

    path(
        "period-definitions/",
        include(
            "apps.timetable.period_definitions.urls"
        )
    ),

    path(
        "resource-allocations/",
        include(
            "apps.timetable.resource_allocations.urls"
        )
    ),

    path(
        "room-allocations/",
        include(
            "apps.timetable.room_allocations.urls"
        )
    ),

    path(
        "subject-constraints/",
        include(
            "apps.timetable.subject_constraints.urls"
        )
    ),

    path(
        "subject-requirements/",
        include(
            "apps.timetable.subject_requirements.urls"
        )
    ),

    path(
        "substitute-assignments/",
        include(
            "apps.timetable.substitute_assignments.urls"
        )
    ),

    path(
        "teacher-availabilities/",
        include(
            "apps.timetable.teacher_availabilities.urls"
        )
    ),

    path(
        "teacher-preferences/",
        include(
            "apps.timetable.teacher_preferences.urls"
        )
    ),

    path(
        "teacher-workloads/",
        include(
            "apps.timetable.teacher_workloads.urls"
        )
    ),

    path(
        "timetables/",
        include(
            "apps.timetable.timetables.urls"
        )
    ),

    path(
        "timetable-approvals/",
        include(
            "apps.timetable.timetable_approvals.urls"
        )
    ),

    path(
        "timetable-audit-logs/",
        include(
            "apps.timetable.timetable_audit_logs.urls"
        )
    ),

    path(
        "timetable-conflicts/",
        include(
            "apps.timetable.timetable_conflicts.urls"
        )
    ),

    path(
        "timetable-entries/",
        include(
            "apps.timetable.timetable_entries.urls"
        )
    ),

    path(
        "timetable-publications/",
        include(
            "apps.timetable.timetable_publications.urls"
        )
    ),

    path(
        "timetable-versions/",
        include(
            "apps.timetable.timetable_versions.urls"
        )
    ),

    path(
        "working-days/",
        include(
            "apps.timetable.working_days.urls"
        )
    ),

]