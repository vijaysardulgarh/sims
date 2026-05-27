# =============================================================================
# associations/urls.py
# =============================================================================

from django.urls import (
    path,
    include
)

urlpatterns = [

    # =========================================================================
    # ASSOCIATIONS
    # =========================================================================

    path(
        "associations/",
        include("apps.associations.associations.urls")
    ),

    # =========================================================================
    # ASSOCIATION ROLES
    # =========================================================================

    path(
        "association-roles/",
        include("apps.associations.association_roles.urls")
    ),

    # =========================================================================
    # STAFF ROLE ASSIGNMENTS
    # =========================================================================

    path(
        "staff-role-assignments/",
        include(
            "apps.associations.staff_association_role_assignments.urls"
        )
    ),

    # =========================================================================
    # STUDENT ROLE ASSIGNMENTS
    # =========================================================================

    path(
        "student-role-assignments/",
        include(
            "apps.associations.student_association_role_assignments.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION MEMBERS
    # =========================================================================

    path(
        "association-members/",
        include(
            "apps.associations.association_members.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION MEETINGS
    # =========================================================================

    path(
        "association-meetings/",
        include(
            "apps.associations.association_meetings.urls"
        )
    ),

    # =========================================================================
    # SMC MEMBERS
    # =========================================================================

    path(
        "smc-members/",
        include(
            "apps.associations.smc_members.urls"
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