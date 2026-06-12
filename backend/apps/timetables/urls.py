from django.urls import (
    include,
    path,
)

urlpatterns = [

    path(
        "bell-schedules/",
        include(
            "apps.timetables.bell_schedules.urls"
        )
    ),

    path(
        "exam-timetables/",
        include(
            "apps.timetables.exam_timetables.urls"
        )
    ),

    path(
        "exam-timetable-entries/",
        include(
            "apps.timetables.exam_timetable_entries.urls"
        )
    ),

    path(
        "period-definitions/",
        include(
            "apps.timetables.period_definitions.urls"
        )
    ),

    path(
        "resource-allocations/",
        include(
            "apps.timetables.resource_allocations.urls"
        )
    ),

    path(
        "room-allocations/",
        include(
            "apps.timetables.room_allocations.urls"
        )
    ),

    path(
        "subject-constraints/",
        include(
            "apps.timetables.subject_constraints.urls"
        )
    ),

    path(
        "subject-requirements/",
        include(
            "apps.timetables.subject_requirements.urls"
        )
    ),

    path(
        "substitute-assignments/",
        include(
            "apps.timetables.substitute_assignments.urls"
        )
    ),

    path(
        "teacher-availabilities/",
        include(
            "apps.timetables.teacher_availabilities.urls"
        )
    ),

    path(
        "teacher-preferences/",
        include(
            "apps.timetables.teacher_preferences.urls"
        )
    ),

    path(
        "teacher-workloads/",
        include(
            "apps.timetables.teacher_workloads.urls"
        )
    ),

    path(
        "timetables/",
        include(
            "apps.timetables.timetables.urls"
        )
    ),

    path(
        "timetable-approvals/",
        include(
            "apps.timetables.timetable_approvals.urls"
        )
    ),

    path(
        "timetable-audit-logs/",
        include(
            "apps.timetables.timetable_audit_logs.urls"
        )
    ),

    path(
        "timetable-conflicts/",
        include(
            "apps.timetables.timetable_conflicts.urls"
        )
    ),

    path(
        "timetable-entries/",
        include(
            "apps.timetables.timetable_entries.urls"
        )
    ),

    path(
        "timetable-publications/",
        include(
            "apps.timetables.timetable_publications.urls"
        )
    ),

    path(
        "timetable-versions/",
        include(
            "apps.timetables.timetable_versions.urls"
        )
    ),

    path(
        "working-days/",
        include(
            "apps.timetables.working_days.urls"
        )
    ),

    path(
    "timetable-designer/",
    include(
        "apps.timetables.timetable_designer.urls"
    )
),

]