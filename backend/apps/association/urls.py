# =============================================================================
# apps/associations/urls.py
# =============================================================================

from django.urls import (
    include,
    path,
)

urlpatterns = [

    # =========================================================================
    # ASSOCIATIONS
    # =========================================================================

    path(

        "groups/",

        include(
            "apps.associations.groups.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION ROLES
    # =========================================================================

    path(

        "roles/",

        include(
            "apps.associations.roles.urls"
        )
    ),

    # =========================================================================
    # STAFF ASSOCIATION ROLE ASSIGNMENTS
    # =========================================================================

    path(

        "staff-role-assignments/",

        include(
            "apps.associations.staff_association_role_assignments.urls"
        )
    ),

    # =========================================================================
    # STUDENT ASSOCIATION ROLE ASSIGNMENTS
    # =========================================================================

    path(

        "student-role-assignments/",

        include(
            "apps.associations.student_association_role_assignments.urls"
        )
    ),

    # =========================================================================
    # MEMBERS
    # =========================================================================

    path(

        "members/",

        include(
            "apps.associations.members.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION MEETINGS
    # =========================================================================

    path(

        "meetings/",

        include(
            "apps.associations.meetings.urls"
        )
    ),

    # =========================================================================
    # SCHOOL MANAGEMENT COMMITTEE MEMBERS
    # =========================================================================

    path(

        "smc/",

        include(
            "apps.associations.smc.urls"
        )
    ),

    # =========================================================================
    # EXTRACURRICULAR ACTIVITIES
    # =========================================================================

    path(

        "extracurricular-activities/",

        include(
            "apps.associations.extracurricular_activities.urls"
        )
    ),
]